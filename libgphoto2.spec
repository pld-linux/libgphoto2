#
# Conditional build:
%bcond_with	apidocs		# without documentation which needed gtk-doc and TeX
%bcond_without	baudboy		# use lockdev library instead of baudboy
#
Summary:	Libraries for digital cameras
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Summary(pt_BR):	GNU Photo - programa GNU para câmeras digitais
Name:		libgphoto2
Version:	2.2.0
Release:	2
License:	LGPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.gz
# Source0-md5:	33aca2d04917287472424fe73694cd3d
Source1:	%{name}_port.pl.po
Source2:	%{name}-pl.po
Patch0:		%{name}-pmake.patch
Patch1:		%{name}-print_dev_rules.patch
URL:		http://www.gphoto.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	gettext-devel >= 0.14.1
%{?with_apidocs:BuildRequires:	gtk-doc >= 0.10}
BuildRequires:	libexif-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libusb-devel
%{?with_baudboy:BuildRequires:	lockdev-baudboy-devel}
%{!?with_baudboy:BuildRequires:	lockdev-devel >= 1.0.2}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Provides:	gphoto2-lib
Obsoletes:	gphoto2-lib
Conflicts:	gphoto2 < 2.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	libexif-devel
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
%patch1 -p1

cp %{SOURCE1} libgphoto2_port/po/pl.po
sed -i -e 's/\(ALL_LINGUAS=.*\)"$/\1 pl"/' libgphoto2_port/configure.in
rm -f libgphoto2_port/po/stamp-po
cp %{SOURCE2} po/pl.po
sed -i -e 's/\(ALL_LINGUAS=.*\)"$/\1 pl"/' configure.in
rm -f po/stamp-po

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
	%{?with_apidocs:apidocdir=%{_gtkdocdir}}

%find_lang %{name} --all-name

# prepare docs
install -d docs
cp --parents \
	camlibs/adc65/{Changelog,README,TODO} \
	camlibs/agfa-cl20/{ChangeLog,RANDOM,README,STATUS} \
	camlibs/aox/{ChangeLog,README} \
	camlibs/canon/{ChangeLog,README,TODO} \
	camlibs/casio/{ChangeLog,PROTOCOL.txt} \
	camlibs/digigr8/{ChangeLog,README} \
	camlibs/digita/ChangeLog \
	camlibs/dimera/{CREDITS,ChangeLog,Protocol.txt,TODO} \
	camlibs/directory/ChangeLog \
	camlibs/enigma13/{ChangeLog,README,STATUS,protocol.txt} \
	camlibs/fuji/{ChangeLog,PROTOCOL} \
	camlibs/gsmart300/{ChangeLog,README} \
	camlibs/hp215/ChangeLog \
	camlibs/iclick/{ChangeLog,README} \
	camlibs/jamcam/{ChangeLog,README} \
	camlibs/jd11/{ChangeLog,jd11.html} \
	camlibs/kodak/CAMERAS \
	camlibs/kodak/dc120/ChangeLog \
	camlibs/kodak/dc210/{ChangeLog,TODO} \
	camlibs/kodak/dc240/ChangeLog \
	camlibs/kodak/dc3200/ChangeLog \
	camlibs/kodak/ez200/Protocol.txt \
	camlibs/konica/{ChangeLog,EXPERTS,README,TODO} \
	camlibs/largan/lmini/{ChangeLog,README} \
	camlibs/lg_gsm/{ChangeLog,README} \
	camlibs/mars/{ChangeLog,README,protocol.txt} \
	camlibs/minolta/NEWER_MINOLTAS \
	camlibs/minolta/dimagev/README \
	camlibs/mustek/{AUTHOR,ChangeLog,README} \
	camlibs/panasonic/{ChangeLog,README} \
	camlibs/panasonic/coolshot/{ChangeLog,README} \
	camlibs/panasonic/l859/{ChangeLog,README,TODO} \
	camlibs/pccam300/{ChangeLog,README} \
	camlibs/pccam600/{ChangeLog,README} \
	camlibs/polaroid/{ChangeLog,*.html} \
	camlibs/ptp2/{ChangeLog,README,TODO} \
	camlibs/ricoh/{ChangeLog,g3.txt} \
	camlibs/samsung/ChangeLog \
	camlibs/sierra/{ChangeLog,PROTOCOL} \
	camlibs/sipix/{ChangeLog,*.txt,web2.html} \
	camlibs/smal/{ChangeLog,README} \
	camlibs/sonix/README \
	camlibs/sonydscf1/{ChangeLog,README,readme,todo} \
	camlibs/sonydscf55/{ChangeLog,TODO} \
	camlibs/soundvision/{ChangeLog,README} \
	camlibs/spca50x/{ChangeLog*,README} \
	camlibs/sq905/{ChangeLog,README,TODO} \
	camlibs/stv0674/{Changelog,Protocol} \
	camlibs/stv0680/{680_comm*,CREDITS,ChangeLog,README.pdf} \
	camlibs/sx330z/ChangeLog \
	camlibs/toshiba/pdrm11/README \
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
%doc AUTHORS CHANGES ChangeLog NEWS README TESTERS docs/*
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
%attr(755,root,root) %{_libdir}/libgphoto2/print-udev-rules
%attr(755,root,root) %{_libdir}/libgphoto2/print-usb-usermap
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
