#
# Conditional build:
%bcond_with	apidocs		# API documentation (currently broken)
%bcond_without	baudboy		# use lockdev library instead of baudboy
%bcond_with	canon20d	# Canon EOS 20D experimental code 
%bcond_with	canonupload	# Canon upload experimental code 
#
Summary:	Libraries for digital cameras
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Summary(pt_BR):	GNU Photo - programa GNU para câmeras digitais
Name:		libgphoto2
Version:	2.3.1
Release:	3
License:	LGPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	37f85e34e5b6031ddf6cac8b8782ac4f
Patch0:		%{name}-pmake.patch
URL:		http://www.gphoto.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	dbus-devel >= 0.31
BuildRequires:	gettext-devel >= 0.14.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 0.10}
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libusb-devel >= 0.1.5
%{?with_baudboy:BuildRequires:	lockdev-baudboy-devel}
%{!?with_baudboy:BuildRequires:	lockdev-devel >= 1.0.2}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libexif >= 1:0.6.13
Provides:	gphoto2-lib
Obsoletes:	gphoto2-lib
Conflicts:	gphoto2 < 2.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

# PKGCONFIG changed during configures
%undefine	configure_cache

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
Requires:	%{name} = %{version}-%{release}
%{?with_apidocs:Requires:	gtk-doc-common}
Requires:	libexif-devel >= 1:0.6.13
Requires:	libltdl-devel
Requires:	libusb-devel
%{!?with_baudboy:Requires:	lockdev-devel}
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
Requires:	%{name}-devel = %{version}-%{release}
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

%package port-serial
Summary:	Serial port plugin for libgphoto2
Summary(pl):	Wtyczka obs³ugi portu szeregowego dla libgphoto2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_baudboy:Requires:	lockdev-baudboy}

%description port-serial
Serial port plugin for libgphoto2, needed to access cameras connected
through serial port.

%description port-serial -l pl
Wtyczka obs³ugi portu szeregowego dla libgphoto2, potrzebna do
wspó³pracy z aparatami pod³±czonymi przez port szeregowy.

%prep
%setup -q
%patch0 -p1

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__aclocal} -I libgphoto2_port/m4
%{__autoconf}
%{__automake}
cd libgphoto2_port
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd ..

CFLAGS="%{rpmcflags}%{?with_canon20d: -DCANON_EXPERIMENTAL_20D}%{?with_canonupload: -DCANON_EXPERIMENTAL_UPLOAD}"
%configure \
	%{!?with_baudboy:--disable-baudboy} \
	--disable-resmgr \
	--disable-ttylock \
	%{?with_apidocs:--enable-docs} \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	udevscriptdir=%{_libdir}/libgphoto2 \
	%{?with_apidocs:apidocdir=%{_gtkdocdir}}

%find_lang %{name} --all-name

# prepare docs
install -d docs
cp --parents \
	camlibs/adc65/{Changelog,README.adc65,TODO} \
	camlibs/agfa-cl20/{ChangeLog,RANDOM,README.agfa-cl20,STATUS} \
	camlibs/aox/{ChangeLog,README.aox} \
	camlibs/barbie/README.barbie \
	camlibs/canon/{ChangeLog,README.canon,TODO} \
	camlibs/casio/{ChangeLog,PROTOCOL.txt} \
	camlibs/clicksmart310/README.clicksmart310 \
	camlibs/digigr8/{ChangeLog,README.digigr8} \
	camlibs/digita/ChangeLog \
	camlibs/dimera/{CREDITS,ChangeLog,Protocol.txt,TODO} \
	camlibs/directory/ChangeLog \
	camlibs/enigma13/{ChangeLog,README.enigma13,STATUS,protocol.txt} \
	camlibs/fuji/{ChangeLog,PROTOCOL} \
	camlibs/gsmart300/{ChangeLog,README.gsmart300} \
	camlibs/hp215/ChangeLog \
	camlibs/iclick/{ChangeLog,README.iclick} \
	camlibs/jamcam/{ChangeLog,README.jamcam} \
	camlibs/jd11/{ChangeLog,jd11.html} \
	camlibs/kodak/CAMERAS \
	camlibs/kodak/dc120/ChangeLog \
	camlibs/kodak/dc210/{ChangeLog,TODO} \
	camlibs/kodak/dc240/ChangeLog \
	camlibs/kodak/dc3200/ChangeLog \
	camlibs/kodak/ez200/Protocol.txt \
	camlibs/konica/{ChangeLog,EXPERTS,README.konica,TODO} \
	camlibs/largan/lmini/{ChangeLog,README.largan-lmini} \
	camlibs/lg_gsm/{ChangeLog,README.lg_gsm} \
	camlibs/mars/{ChangeLog,README.mars,protocol.txt} \
	camlibs/minolta/NEWER_MINOLTAS \
	camlibs/minolta/dimagev/README.minolta-dimagev \
	camlibs/mustek/{AUTHOR,ChangeLog,README.mustek} \
	camlibs/panasonic/{ChangeLog,README.panasonic} \
	camlibs/panasonic/coolshot/{ChangeLog,README.panasonic-coolshot} \
	camlibs/panasonic/l859/{ChangeLog,README.panasonic-l859,TODO} \
	camlibs/pccam300/{ChangeLog,README.pccam300} \
	camlibs/pccam600/{ChangeLog,README.pccam600} \
	camlibs/polaroid/{ChangeLog,*.html} \
	camlibs/ptp2/{ChangeLog,PTPIP.TXT,README.ptp2,TODO,ptpip.html} \
	camlibs/ricoh/{ChangeLog,g3.txt} \
	camlibs/samsung/ChangeLog \
	camlibs/sierra/{ChangeLog,PROTOCOL} \
	camlibs/sipix/{ChangeLog,*.txt,web2.html} \
	camlibs/smal/{ChangeLog,README.smal} \
	camlibs/sonix/{ChangeLog,README.sonix} \
	camlibs/sonydscf1/{ChangeLog,README.sonydscf1,todo} \
	camlibs/sonydscf55/{ChangeLog,TODO} \
	camlibs/soundvision/{ChangeLog,README.soundvision} \
	camlibs/spca50x/{ChangeLog*,README.spca50x} \
	camlibs/sq905/{ChangeLog,README.913C,README.sq905,TODO} \
	camlibs/stv0674/{Changelog,Protocol} \
	camlibs/stv0680/{680_comm*,CREDITS,ChangeLog,README.pdf} \
	camlibs/sx330z/ChangeLog \
	camlibs/toshiba/pdrm11/README.toshiba-pdrm11 \
	libgphoto2_port/{AUTHORS,ChangeLog} \
	libgphoto2_port/disk/ChangeLog \
	docs

rm -f $RPM_BUILD_ROOT%{_libdir}/libgphoto2/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libgphoto2_port/*/*.a
# kill unpackaged files
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libgphoto{2,2_port}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TESTERS docs/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

# camera plugins
%dir %{_libdir}/libgphoto2
%dir %{_libdir}/libgphoto2/%{version}
%attr(755,root,root) %{_libdir}/libgphoto2/%{version}/*.so
%{_libdir}/libgphoto2/%{version}/*.la

# port plugins
%dir %{_libdir}/libgphoto2_port
%dir %{_libdir}/libgphoto2_port/*
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/disk.so
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/ptpip.so
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/usb.so
%{_libdir}/libgphoto2_port/*/disk.la
%{_libdir}/libgphoto2_port/*/ptpip.la
%{_libdir}/libgphoto2_port/*/usb.la

# utilities
%attr(755,root,root) %{_libdir}/libgphoto2/check-ptp-camera
%attr(755,root,root) %{_libdir}/libgphoto2/print-camera-list

%dir %{_datadir}/libgphoto2
%dir %{_datadir}/libgphoto2/%{version}
%dir %{_datadir}/libgphoto2/%{version}/konica
%{_datadir}/libgphoto2/%{version}/konica/english
%lang(fr) %{_datadir}/libgphoto2/%{version}/konica/french
%lang(de) %{_datadir}/libgphoto2/%{version}/konica/german
%lang(ja) %{_datadir}/libgphoto2/%{version}/konica/japanese
%lang(ko) %{_datadir}/libgphoto2/%{version}/konica/korean
%lang(es) %{_datadir}/libgphoto2/%{version}/konica/spanish

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gphoto2*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/gphoto2
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*
%{?with_apidocs:%{_gtkdocdir}/*}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files port-serial
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/serial.so
%{_libdir}/libgphoto2_port/*/serial.la
