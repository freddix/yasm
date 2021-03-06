Summary:	The YASM Modular Assembler
Name:		yasm
Version:	1.3.0
Release:	1
License:	distributable (BSD, GPL, LGPL, Artistic; see COPYING)
Group:		Development/Tools
Source0:	http://www.tortall.net/projects/yasm/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fc9e586751ff789b34b1f21d572d96af
URL:		http://www.tortall.net/projects/yasm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yasm is a complete rewrite of the NASM assembler under the "new"
BSD License (some portions are under other licenses, see COPYING for
details). It is designed from the ground up to allow for multiple
assembler syntaxes to be supported (eg, NASM, TASM, GAS, etc.) in
addition to multiple output object formats and even multiple
instruction sets. Another primary module of the overall design is an
optimizer module.

%package -n libyasm-devel
Summary:	Header files and static libyasm library
Group:		Development/Libraries
License:	BSD+Artistic or LGPL or GPL (see COPYING)

%description -n libyasm-devel
Header files and static libyasm library.

%prep
%setup -q

# Use a larger hash table size
# Increases compilation speed of files with a large number of macros
# by around 20x.
%{__sed} -i 's/#define NHASH 31/#define NHASH 4096/' \
    modules/preprocs/nasm/nasm-pp.c

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug}
%{__make} -j1 all check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD.txt COPYING
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[17]/*

%files -n libyasm-devel
%defattr(644,root,root,755)
%doc AUTHORS BSD.txt COPYING
%{_libdir}/libyasm.a
%{_includedir}/libyasm*.h
%{_includedir}/libyasm

