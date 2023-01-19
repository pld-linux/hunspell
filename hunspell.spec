Summary:	Hunspell - a spell checker and morphological analyzer
Summary(hu.UTF-8):	Hunspell egy helyesírás-ellenőrző és morfológiai elemző könyvtár és program
Summary(pl.UTF-8):	hunspell - narzędzie do sprawdzania pisowni i analizy morfologicznej
Name:		hunspell
Version:	1.7.2
Release:	2
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Applications/Text
#Source0Download: https://github.com/hunspell/hunspell/releases
Source0:	https://github.com/hunspell/hunspell/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7102d7435f9a89b562dacf7d5be5458e
Patch0:		%{name}-install.patch
URL:		http://hunspell.github.io/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
OpenOffice.org UNO module.

This package contains base programs (hunspell, hzip, hunzip).

%description -l hu.UTF-8
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

Ten pakiet zawiera podstawowe programy (hunspell, hzip, hunzip).

%package tools
Summary:	hunspell tools
Summary(pl.UTF-8):	Narzędzia hunspella
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Obsoletes:	myspell-tools < 3.2

%description tools
This package contains hunspell utilities, including munch and unmunch.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzia dla hunspella, w tym programy munch i
unmunch.

%package libs
Summary:	Hunspell spell checker and morphological analyzer library
Summary(pl.UTF-8):	Biblioteka Hunspell do sprawdzania pisowni i analizy morfologicznej
Group:		Libraries

%description libs
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
OpenOffice.org UNO module.

This package contains the shared library.

%description libs -l pl.UTF-8
hunspell to biblioteka oraz program do sprawdzania pisowni i analizy
morfologicznej zaprojektowany dla języków z bogatą morfologią i
zkomplikowanym składaniem słów lub kodowaniem znaków. Interfejsy
hunspella to: interfejs terminalowy w stylu Ispella korzystający z
biblioteki Curses, interfejs potokowy Ispella, moduł UNO
OpenOffice.org.

Ten pakiet zawiera bibliotekę współdzieloną.

%package devel
Summary:	Files for developing with hunspell
Summary(pl.UTF-8):	Pliki do programowania z użyciem hunspella
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Includes and definitions for developing with hunspell.

%description devel -l hu.UTF-8
Header-fájlok és definíciók hunspell-lel való fejlesztéshez.

%description devel -l pl.UTF-8
Pliki nagłówkowe i definicje do programowania z użyciem hunspella.

%package static
Summary:	Static hunspell library
Summary(pl.UTF-8):	Statyczna biblioteka hunspella
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hunspell library.

%description static -l hu.UTF-8
Hunspell statikus könyvtár.

%description static -l pl.UTF-8
Statyczna biblioteka hunspella.

%prep
%setup -q
%patch0 -p1

# stale file in source tarball (even though *.gmo are not included), breaks locale install
%{__rm} po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	--with-readline \
	--with-ui

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libhunspell-*.la

# not supported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie
# almost a copy of pt (one word difference as of 1.7.2)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pt_PT
# unify names
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{zh_Hans,zh_CN}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{zh_Hant,zh_TW}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hunspell
%attr(755,root,root) %{_bindir}/hunzip
%attr(755,root,root) %{_bindir}/hzip
%{_mandir}/man1/hunzip.1*
%{_mandir}/man1/hzip.1*
%{_mandir}/man1/hunspell.1*
%{_mandir}/man5/hunspell.5*
%lang(hu) %{_mandir}/hu/man1/hunspell.1*
%lang(hu) %{_mandir}/hu/man5/hunspell.5*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/affixcompress
%attr(755,root,root) %{_bindir}/analyze
%attr(755,root,root) %{_bindir}/chmorph
%attr(755,root,root) %{_bindir}/ispellaff2myspell
%attr(755,root,root) %{_bindir}/makealias
%attr(755,root,root) %{_bindir}/munch
%attr(755,root,root) %{_bindir}/unmunch
%attr(755,root,root) %{_bindir}/wordforms
%attr(755,root,root) %{_bindir}/wordlist2hunspell

%files libs
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md THANKS license.hunspell license.myspell
%attr(755,root,root) %{_libdir}/libhunspell-1.7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhunspell-1.7.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhunspell-1.7.so
%{_includedir}/hunspell
%{_pkgconfigdir}/hunspell.pc
%{_mandir}/man3/hunspell.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhunspell-1.7.a
