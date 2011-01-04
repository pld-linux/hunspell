# TODO:
# $ LC_ALL=C hunspell -d hu_HU foo
# Hunspell has been compiled without Ncurses user interface.
Summary:	Hunspell - a spell checker and morphological analyzer library
Summary(hu.UTF-8):	Hunspell egy helyesírás-ellenőrző és morfológiai elemző könyvtár és program
Summary(pl.UTF-8):	hunspell - biblioteka do sprawdzania pisowni i analizy morfologicznej
Name:		hunspell
Version:	1.2.13
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz
# Source0-md5:	a84a1ea76980069331f3bd6c5c3f0aac
Patch0:		%{name}-as-needed.patch
URL:		http://hunspell.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libhunspell.so.1()(64bit)
%else
Provides:	libhunspell.so.1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hunspell is a spell checker and morphological analyzer library and
program designed for languages with rich morphology and complex word
compounding or character encoding. Hunspell interfaces: Ispell-like
terminal interface using Curses library, Ispell pipe interface,
OpenOffice.org UNO module.

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

# NOTE: munch,unmunch collide with myspell-tools
%package tools
Summary:	hunspell tools
Summary(pl.UTF-8):	Narzędzia hunspella
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains hunspell utilities, including munch and unmunch.

%description tools -l pl.UTF-8
Ten pakiet zawiera narzędzia dla hunspella, w tym programy munch i
unmunch.

%package devel
Summary:	Files for developing with hunspell
Summary(pl.UTF-8):	Pliki do programowania z użyciem hunspella
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
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

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure \
	--with-ui \
	--with-readline

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s $(basename $RPM_BUILD_ROOT%{_libdir}/libhunspell-1.2.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libhunspell.so.1
%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_bindir}/example

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS AUTHORS.myspell COPYING ChangeLog NEWS README README.myspell THANKS license.hunspell license.myspell
%attr(755,root,root) %{_bindir}/hunspell
%attr(755,root,root) %{_bindir}/hunzip
%attr(755,root,root) %{_bindir}/hzip
%attr(755,root,root) %{_libdir}/libhunspell-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libhunspell-1.2.so.0
%attr(755,root,root) %{_libdir}/libhunspell.so.1
%{_mandir}/man1/hunzip.1*
%{_mandir}/man1/hzip.1*
%{_mandir}/man1/hunspell.1*
%{_mandir}/man4/hunspell.4*
%lang(hu) %{_mandir}/hu/man1/hunspell.1*
%lang(hu) %{_mandir}/hu/man4/hunspell.4*

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhunspell-1.2.so
%{_libdir}/libhunspell-1.2.la
%{_libdir}/libparsers.a
%{_includedir}/hunspell
%{_pkgconfigdir}/hunspell.pc
%{_mandir}/man3/hunspell.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libhunspell-1.2.a