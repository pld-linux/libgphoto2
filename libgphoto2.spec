#
# Conditional build:
%bcond_with	apidocs		# API documentation (currently broken)
%bcond_without	baudboy		# use lockdev library instead of baudboy
%bcond_with	canonupload	# Canon upload experimental code
%bcond_with	hal		# build HAL support
%bcond_without	static_libs	# static libraries
#
Summary:	Libraries for digital cameras
Summary(es.UTF-8):	Foto GNU (gphoto) Release 2
Summary(pl.UTF-8):	Biblioteki obsługi kamer cyfrowych
Summary(pt_BR.UTF-8):	GNU Photo - programa GNU para câmeras digitais
Name:		libgphoto2
Version:	2.4.12
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	735c50ebb15cb8be61bac400ee4afb1e
Patch0:		%{name}-mode-owner-group.patch
Patch1:		%{name}-IXANY.patch
Patch2:		%{name}-increase_max_entries.patch
Patch3:		%{name}-pl.po-update.patch
URL:		http://www.gphoto.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	dbus-devel >= 0.31
BuildRequires:	gd-devel
BuildRequires:	gettext-devel >= 0.14.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 0.10}
%{?with_hal:BuildRequires:	hal-devel >= 0.5.0}
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libjpeg-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libusb-devel >= 1.0.0
%{?with_baudboy:BuildRequires:	lockdev-baudboy-devel}
%{!?with_baudboy:BuildRequires:	lockdev-devel >= 1.0.2}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libexif >= 1:0.6.13
Provides:	gphoto2-lib
Obsoletes:	gphoto2-lib
Conflicts:	gphoto2 < 2.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles		%{_libdir}/libgphoto2/.*\\.la %{_libdir}/libgphoto2_port/.*\\.la

# PKGCONFIG changed during configures
%undefine	configure_cache

%description
Libraries for digital cameras.

%description -l es.UTF-8
Foto GNU (gphoto).

%description -l pl.UTF-8
Biblioteki obsługi kamer cyfrowych.

%description -l pt_BR.UTF-8
O programa gphoto faz parte do projeto GNOME e é uma interface para
uma grande variedade de câmeras fotográficas digitais.

%package devel
Summary:	Header files for libgphoto2
Summary(es.UTF-8):	Archivos de deserrolo de libgphoto2
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgphoto2
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento do libgphoto2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_apidocs:Requires:	gtk-doc-common}
Requires:	libexif-devel >= 1:0.6.13
Requires:	libltdl-devel
Requires:	libusb-compat-devel >= 0.1
%{!?with_baudboy:Requires:	lockdev-devel}
Obsoletes:	gphoto2-devel
Obsoletes:	gphoto2-lib-devel

%description devel
Header files for libgphoto2.

%description devel -l es.UTF-8
Archivos de desarrolo de libgphoto2.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libgphoto2.

%description devel -l pt_BR.UTF-8
Arquivos de desenvolvimento do libgphoto2.

%package static
Summary:	Static version of libgphoto2
Summary(es.UTF-8):	Archivos de deserrolo de libgphoto2
Summary(pl.UTF-8):	Statyczna wersja libgphoto2
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento do libgphoto2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gphoto2-lib-static
Obsoletes:	gphoto2-static

%description static
Static version of libgphoto2.

%description static -l es.UTF-8
Archivos de desarrolo de libgphoto2.

%description static -l pl.UTF-8
Statyczna wersja libgphoto2.

%description static -l pt_BR.UTF-8
Arquivos de desenvolvimento do libgphoto2.

%package port-serial
Summary:	Serial port plugin for libgphoto2
Summary(pl.UTF-8):	Wtyczka obsługi portu szeregowego dla libgphoto2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_baudboy:Requires:	lockdev-baudboy}

%description port-serial
Serial port plugin for libgphoto2, needed to access cameras connected
through serial port.

%description port-serial -l pl.UTF-8
Wtyczka obsługi portu szeregowego dla libgphoto2, potrzebna do
współpracy z aparatami podłączonymi przez port szeregowy.

%package -n udev-libgphoto2
Summary:	Userspace support for digital cameras
Summary(pl.UTF-8):	Wsparcie dla kamer cyfrowych w przestrzeni użytkownika
Group:		Applications/System
Requires:	libusb-compat >= 0.1
%if "%{pld_release}" == "ti"
Requires:	udev-core >= 1:124-3
%else
Requires:	udev-core >= 1:136
%endif
Provides:	udev-digicam
Obsoletes:	hal-gphoto
%{!?with_hal:Obsoletes:	hal-libgphoto2}
Obsoletes:	hotplug-digicam
Obsoletes:	udev-digicam

%description -n udev-libgphoto2
Set of Udev rules to handle digital cameras in userspace.

%description -n udev-libgphoto2 -l pl.UTF-8
Zestaw reguł Udev do obsługi kamer cyfrowych w przestrzeni
użytkownika.

%package -n hal-libgphoto2
Summary:	Userspace support for digital cameras
Summary(pl.UTF-8):	Wsparcie dla kamer cyfrowych w przestrzeni użytkownika
Group:		Applications/System
Requires:	hal >= 0.5.9-2
Requires:	udev-libgphoto2

%description -n hal-libgphoto2
HAL device information file to handle digital cameras in userspace.

%description -n hal-libgphoto2 -l pl.UTF-8
Plik z informacjami o urządzeniach HAL-a do obsługi kamer cyfrowych
w przestrzeni użytkownika.

%prep
%setup -q
%patch0 -p1
%ifarch alpha
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

%{__rm} po/stamp-po libgphoto2_port/po/stamp-po

%build
# supplied libtool is broken (relink)
%{__libtoolize}
%{__aclocal} -I auto-m4 -I m4m
%{__autoconf}
%{__automake}
cd libgphoto2_port
%{__libtoolize}
%{__aclocal} -I auto-m4 -I m4
%{__autoconf}
%{__automake}
cd ..

CFLAGS="%{rpmcflags}%{?with_canonupload: -DCANON_EXPERIMENTAL_UPLOAD}"
%configure \
	%{!?with_baudboy:--disable-baudboy} \
	--disable-resmgr \
	--disable-ttylock \
	%{?with_apidocs:--enable-docs} \
	%{?with_static_libs:--enable-static} \
	--with%{!?with_hal:out}-hal \
	%{?with_apidocs:--with-html-dir=%{_gtkdocdir}} \
	--without-libusb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	udevscriptdir=/lib/udev \
	%{?with_apidocs:apidocdir=%{_gtkdocdir}}

%find_lang %{name} --all-name

# prepare docs
install -d docs
cp --parents \
	camlibs/adc65/{Changelog,README.adc65,TODO} \
	camlibs/agfa-cl20/{ChangeLog,RANDOM,README.agfa-cl20,STATUS} \
	camlibs/aox/README.aox \
	camlibs/barbie/{ChangeLog,Protocol.txt} \
	camlibs/canon/{ChangeLog,README.canon,TODO} \
	camlibs/casio/{ChangeLog,PROTOCOL.txt} \
	camlibs/clicksmart310/README.clicksmart310 \
	camlibs/digigr8/{ChangeLog,README.*} \
	camlibs/digita/ChangeLog \
	camlibs/dimera/{CREDITS,Protocol.txt,TODO} \
	camlibs/directory/ChangeLog \
	camlibs/enigma13/{ChangeLog,README.enigma13,STATUS,protocol.txt} \
	camlibs/fuji/{ChangeLog,PROTOCOL} \
	camlibs/gsmart300/{ChangeLog,README.gsmart300} \
	camlibs/hp215/{ChangeLog,PROTOCOL} \
	camlibs/iclick/{ChangeLog,README.iclick} \
	camlibs/jamcam/{ChangeLog,README.jamcam} \
	camlibs/jd11/{ChangeLog,jd11.html} \
	camlibs/jl2005a/README.jl2005a \
	camlibs/jl2005c/README.jl2005c \
	camlibs/kodak/CAMERAS \
	camlibs/kodak/d*/ChangeLog \
	camlibs/kodak/ez200/{ChangeLog,Protocol.txt} \
	camlibs/konica/{ChangeLog,EXPERTS,README.konica,TODO,qm150.txt} \
	camlibs/largan/lmini/{ChangeLog,README.largan-lmini} \
	camlibs/lg_gsm/{ChangeLog,README.lg_gsm} \
	camlibs/mars/{ChangeLog,README.mars,protocol.txt} \
	camlibs/minolta/NEWER_MINOLTAS \
	camlibs/minolta/dimagev/README.minolta-dimagev \
	camlibs/mustek/{AUTHOR,ChangeLog,README.mustek,STATUS} \
	camlibs/panasonic/{ChangeLog,README.panasonic} \
	camlibs/panasonic/coolshot/{ChangeLog,README.panasonic-coolshot} \
	camlibs/panasonic/l859/{ChangeLog,README.panasonic-l859,TODO} \
	camlibs/pccam300/{ChangeLog,README.pccam300} \
	camlibs/pccam600/{ChangeLog,README.pccam600} \
	camlibs/polaroid/{ChangeLog,*.html} \
	camlibs/ptp2/{ChangeLog,PTPIP.TXT,README.ptp2,TODO,ptpip.html} \
	camlibs/ricoh/{ChangeLog,g3.txt} \
	camlibs/samsung/ChangeLog \
	camlibs/sierra/{ChangeLog,MC-EU1-Protocol.txt,PROTOCOL} \
	camlibs/sipix/{ChangeLog,*.txt,web2.html} \
	camlibs/smal/{ChangeLog,README.smal} \
	camlibs/sonix/{ChangeLog,README.sonix} \
	camlibs/sonydscf1/{ChangeLog,README.sonydscf1} \
	camlibs/sonydscf55/{ChangeLog,TODO} \
	camlibs/soundvision/{BUGS,ChangeLog,README.soundvision} \
	camlibs/spca50x/{ChangeLog*,README.spca50x} \
	camlibs/sq905/{ChangeLog,README.913C,README.sq905,TODO} \
	camlibs/stv0674/{Changelog,Protocol} \
	camlibs/stv0680/{680_comm*,CREDITS,ChangeLog,README.pdf} \
	camlibs/sx330z/ChangeLog \
	camlibs/topfield/ChangeLog \
	camlibs/toshiba/pdrm11/README.toshiba-pdrm11 \
	libgphoto2_port/{AUTHORS,ChangeLog,NEWS,README} \
	libgphoto2_port/disk/ChangeLog \
	docs

# udev
cd packaging/linux-hotplug
install -d $RPM_BUILD_ROOT/lib/udev/rules.d
export CAMLIBS=$RPM_BUILD_ROOT%{_libdir}/%{name}/%{version}

../generic/print-camera-list udev-rules version 136 group usb mode 0660 \
	> $RPM_BUILD_ROOT/lib/udev/rules.d/40-libgphoto2.rules

%if %{with hal}
# hal
install -d $RPM_BUILD_ROOT%{_datadir}/hal/fdi/information/20thirdparty

../generic/print-camera-list hal-fdi | \
	grep -v "<!-- This file was generated" > $RPM_BUILD_ROOT%{_datadir}/hal/fdi/information/20thirdparty/10-camera-libgphoto2.fdi
%endif

%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgphoto2/*/*.a
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgphoto2_port/*/*.a
%endif
# kill unpackaged files
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/libgphoto{2,2_port}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n hal-libgphoto2
%service -q haldaemon restart

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TESTERS docs/*
%attr(755,root,root) %{_libdir}/libgphoto2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgphoto2.so.2
%attr(755,root,root) %{_libdir}/libgphoto2_port.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgphoto2_port.so.0

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
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/usb1.so
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/usbdiskdirect.so
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/usbscsi.so
%{_libdir}/libgphoto2_port/*/disk.la
%{_libdir}/libgphoto2_port/*/ptpip.la
%{_libdir}/libgphoto2_port/*/usb1.la
%{_libdir}/libgphoto2_port/*/usbdiskdirect.la
%{_libdir}/libgphoto2_port/*/usbscsi.la

# utilities
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
%attr(755,root,root) %{_bindir}/gphoto2-config
%attr(755,root,root) %{_bindir}/gphoto2-port-config
%attr(755,root,root) %{_libdir}/libgphoto2.so
%attr(755,root,root) %{_libdir}/libgphoto2_port.so
%{_libdir}/libgphoto2.la
%{_libdir}/libgphoto2_port.la
%{_includedir}/gphoto2
%{_pkgconfigdir}/libgphoto2.pc
%{_pkgconfigdir}/libgphoto2_port.pc
%{_mandir}/man3/libgphoto2.3*
%{_mandir}/man3/libgphoto2_port.3*
%{?with_apidocs:%{_gtkdocdir}/*}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgphoto2.a
%{_libdir}/libgphoto2_port.a
%endif

%files port-serial
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgphoto2_port/*/serial.so
%{_libdir}/libgphoto2_port/*/serial.la

%files -n udev-libgphoto2
%defattr(644,root,root,755)
/lib/udev/rules.d/40-libgphoto2.rules
%attr(755,root,root) /lib/udev/check-ptp-camera

%if %{with hal}
%files -n hal-libgphoto2
%defattr(644,root,root,755)
%{_datadir}/hal/fdi/information/20thirdparty/10-camera-libgphoto2.fdi
%endif
