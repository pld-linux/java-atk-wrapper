Summary:	Java ATK Wrapper is a implementation of ATK by using JNI technic
Summary(pl.UTF-8):	Java ATK Wrapper - implementacja ATK wykorzystująca JNI
Name:		java-atk-wrapper
Version:	0.38.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Java
Source0:	http://ftp.gnome.org/pub/GNOME/sources/java-atk-wrapper/0.38/%{name}-%{version}.tar.xz
# Source0-md5:	3574151e35922c25e3425e9c5b7de8c5
URL:		https://wiki.gnome.org/Accessibility/JavaAtkWrapper
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	at-spi2-atk-devel >= 2.33.1
BuildRequires:	at-spi2-core-devel >= 2.14.0
BuildRequires:	atk-devel >= 1:2.14.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	jdk >= 1.7
BuildRequires:	jpackage-utils
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	at-spi2-core-libs >= 2.14.0
Requires:	at-spi2-atk-libs >= 2.33.1
Requires:	atk >= 1:2.14.0
Requires:	glib2 >= 1:2.32.0
Requires:	jpackage-utils
Requires:	xorg-app-xprop
Obsoletes:	java-access-bridge
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java ATK Wrapper is a implementation of ATK by using JNI technic. It
converts Java Swing events into ATK events, and send these events to
ATK-Bridge.

JAW is part of the Bonobo deprecation project. It will replaces the
former java-access-bridge. By talking to ATK-Bridge, it keeps itself
from being affected by the change of underlying communication
mechanism.

%description -l pl.UTF-8
Java ATK Wrapper to implementacja ATK wykorzystująca technikę JNI.
Przekształca zdarzenia Java Swing na zdarzenia ATK i wysyła je do
interfejsu ATK-Bridge.

JAW to część projektu odchodzenia od Bonobo. Zastąpi poprzedni
java-access-bridge. Dzięki komunikacji z ATK-Bridge pakiet nie jest
zależny od zmiany mechanizmu komunikacji stojącego za interfejsem.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	JAVA_HOME=%{java_home} \
	JDK_SRC=%{java_home} \
	XPROP=/usr/bin/xprop \
	--disable-silent-rules \
	--without-jdk-auto-detect \
	--with-propertiesdir=%{java_home}/jre/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	propertiesdir=%{_javadir} \
	java_atk_wrapperdir=%{_javadir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatk-wrapper.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libatk-wrapper.so
%{_javadir}/accessibility.properties
%{_javadir}/java-atk-wrapper.jar
