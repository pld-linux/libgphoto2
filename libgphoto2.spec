Summary:	Libraries for digital cameras
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Summary(pt_BR):	GNU Photo - programa GNU para câmeras digitais
Name:		libgphoto2
Version:	2.1.1
Release:	2
License:	LGPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5: ec69ffba3dc3d6a6a604fd63b3e1159e
Patch0:		%{name}-pmake.patch
URL:		http://www.gphoto.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	libexif-devel
BuildRequires:	libusb-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	gphoto2-lib
Obsoletes:	gphoto2-lib
Conflicts:	gphoto2 < 2.1.1

%description
Libraries for digital cameras.

%description -l es
Foto GNU (gphoto).

%description -l pl
Biblioteki obs³ugi kamer cyfrowych.

%description -l pt_BR
O programa gphoto faz parte do projeto GNOME e é uma interface para
uma grande variedade de câmeras fotográficas digitais.

%package devel
Summary:	Header files for libgphoto2
Summary(es):	Archivos de deserrolo de libgphoto2
Summary(pl):	Pliki nag³ówkowe dla libgphoto2
Summary(pt_BR):	Arquivos de desenvolvimento do libgphoto2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libexif-devel
Obsoletes:	gphoto2-lib-devel
Obsoletes:	gphoto2-devel

%description devel
Header files for libgphoto2.

%description devel -l es
Archivos de desarrolo de libgphoto2.

%description devel -l pl
Pliki nag³ówkowe dla libgphoto2.

%description devel -l pt_BR
Arquivos de desenvolvimento do libgphoto2.

%package static
Summary:	Static version of libgphoto2
Summary(es):	Archivos de deserrolo de libgphoto2
Summary(pl):	Statyczna wersja libgphoto2
Summary(pt_BR):	Arquivos de desenvolvimento do libgphoto2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	gphoto2-lib-static
Obsoletes:	gphoto2-static

%description static
Static version of libgphoto2.

%description static -l es
Archivos de desarrolo de libgphoto2.

%description static -l pl
Statyczna wersja libgphoto2.

%description static -l pt_BR
Arquivos de desenvolvimento do libgphoto2.

%prep
%setup -q
%patch0 -p1

%build
# supplied libtool is broken (relink)
rm -f missing
%{__libtoolize}
%{__aclocal} -I libgphoto2_port/m4
%{__autoconf}
%{__automake}
cd libgphoto2_port
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd ..

%configure \
	--enable-docs \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	apidocdir=%{_gtkdocdir}

%find_lang %{name} --all-name

# prepare docs
install -d docs
cp --parents \
	libgphoto2_port/{AUTHORS,ChangeLog} \
	camlibs/canon/{ChangeLog,Protocol,README,TODO} \
	camlibs/casio/ChangeLog camlibs/digita/ChangeLog \
	camlibs/dimera/{CREDITS,ChangeLog,Protocol.txt,TODO} \
	camlibs/directory/ChangeLog camlibs/fuji/ChangeLog \
	camlibs/gsmart/{ChangeLog,README} camlibs/jamcam/{ChangeLog,README} \
	camlibs/jd11/{ChangeLog,jd11.html} camlibs/kodak/CAMERAS \
	camlibs/kodak/dc120/ChangeLog camlibs/kodak/dc210/{ChangeLog,TODO} \
	camlibs/kodak/dc240/ChangeLog camlibs/kodak/dc3200/ChangeLog \
	camlibs/konica/{ChangeLog,EXPERTS,README,TODO} \
	camlibs/largan/lmini/{ChangeLog,README} \
	camlibs/minolta/NEWER_MINOLTAS camlibs/minolta/dimagev/README \
	camlibs/mustek/{ChangeLog,README} camlibs/panasonic/{ChangeLog,README} \
	camlibs/panasonic/coolshot/{ChangeLog,README} \
	camlibs/panasonic/l859/{ChangeLog,README,TODO} \
	camlibs/pccam600/{ChangeLog,README} camlibs/polaroid/ChangeLog \
	camlibs/ptp/{ChangeLog,README,TODO} camlibs/ricoh/ChangeLog \
	camlibs/samsung/ChangeLog camlibs/sierra/{ChangeLog,PROTOCOL} \
	camlibs/sipix/{ChangeLog,web2.html} camlibs/sipixblink/ChangeLog \
	camlibs/sonydscf1/{ChangeLog,README,readme,todo} \
	camlibs/sonydscf55/{ChangeLog,TODO} \
	camlibs/soundvision/{ChangeLog,README} \
	camlibs/spca504_flash/{ChangeLog,README} \
	camlibs/stv0680/{680_comm*,CREDITS,ChangeLog,README.pdf} \
	camlibs/sx330z/ChangeLog \
	docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES ChangeLog NEWS README TESTERS docs/*

%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%dir %{_libdir}/gphoto2
%dir %{_libdir}/gphoto2/*
%attr(755,root,root) %{_libdir}/gphoto2/*/libgphoto2_*.so
%{_libdir}/gphoto2/*/libgphoto2_*.la

%dir %{_libdir}/gphoto2_port
%dir %{_libdir}/gphoto2_port/*
%attr(755,root,root) %{_libdir}/gphoto2_port/*/libgphoto2_port_*.so
%{_libdir}/gphoto2_port/*/libgphoto2_port_*.la

%dir %{_libdir}/libgphoto2
%attr(755,root,root) %{_libdir}/libgphoto2/print-usb-usermap

%dir %{_datadir}/libgphoto2
%dir %{_datadir}/libgphoto2/*
%dir %{_datadir}/libgphoto2/*/konica
%{_datadir}/libgphoto2/*/konica/english
%lang(fr) %{_datadir}/libgphoto2/*/konica/french
%lang(de) %{_datadir}/libgphoto2/*/konica/german
%lang(ja) %{_datadir}/libgphoto2/*/konica/japanese
%lang(ko) %{_datadir}/libgphoto2/*/konica/korean
%lang(es) %{_datadir}/libgphoto2/*/konica/spanish

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gphoto2*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/gphoto2
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
