Summary:	Hunspell - a spell checker and morphological analyzer library
Summary(pl.UTF-8):	hunspell - biblioteka do sprawdzania pisowni i analizy morfologicznej
Name:		hunspell
Version:	1.1.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# Source0-md5:	4cf2dfb89dd58392ad5a1183c69eb628
Patch0:		%{name}-sharedlibs.patch
Patch1:		%{name}-defaultdictfromlang.patch
Patch2:		%{name}-capi.patch
URL:		http://hunspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
OpenOffice.org UNO module.

%description -l pl.UTF-8
hunspell to biblioteka oraz program do sprawdzania pisowni i analizy
morfologicznej zaprojektowany dla języków z bogatą morfologią i
zkomplikowanym składaniem słów lub kodowaniem znaków. Interfejsy
hunspella to: interfejs terminalowy w stylu Ispella korzystający z
biblioteki Curses, interfejs potokowy Ispella, moduł UNO
OpenOffice.org.

# NOTE: munch,unmunch collide with myspell-tools
%package tools
Summary:	hunspell tools
Summary(pl.UTF-8):	Narzędzia hunspella
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains munch and unmunch programs.

%description tools -l pl.UTF-8
Ten pakiet zawiera programy munch i unmunch.

%package devel
Summary:	Files for developing with hunspell
Summary(pl.UTF-8):	Pliki do programowania z użyciem hunspella
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Includes and definitions for developing with hunspell.

%description devel -l pl.UTF-8
Pliki nagłówkowe i definicje do programowania z użyciem hunspella.

%package static
Summary:	Static hunspell library
Summary(pl.UTF-8):	Statyczna biblioteka hunspella
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hunspell library.

%description static -l pl.UTF-8
Statyczna biblioteka hunspella.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_bindir}/example

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README README.myspell AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%attr(755,root,root) %{_bindir}/hunmorph
%attr(755,root,root) %{_bindir}/hunspell
%attr(755,root,root) %{_bindir}/hunstem
%attr(755,root,root) %{_libdir}/libhunspell.so.*.*.*
%{_mandir}/man1/hunspell.1*
%{_mandir}/man4/hunspell.4*
%lang(hu) %{_mandir}/hu/man1/hunspell.1*
%lang(hu) %{_mandir}/hu/man4/hunspell.4*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/munch
%attr(755,root,root) %{_bindir}/unmunch

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhunspell.so
%{_libdir}/libhunspell.la
%{_includedir}/%{name}
%{_pkgconfigdir}/hunspell.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libhunspell.a
%{_libdir}/libparsers.a
