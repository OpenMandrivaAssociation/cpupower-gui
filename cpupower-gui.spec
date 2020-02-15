Name:		cpupower-gui
Version:	0.8.0
Release:	1
License:	GPLv3.0
Summary:	   cpupower-gui is a graphical program that is used to change the scaling frequency limits of the cpu, similar to cpupower. 
URL:		https://github.com/vagnum08/cpupower-gui
Group:		System/Kernel and hardware
Source0:	https://github.com/vagnum08/cpupower-gui/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  gettext-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig

Requires:   python
Requires:   gtk+3
Requires:   python-dbus
Requires:   python3dist(pygobject)
Requires:   hicolor-icon-theme
Requires:   polkit

%description
This program is designed to allow you to change the frequency limits of your cpu and its governor. The application is similar in functionality to cpupower but use GTK GUI and CLI.

%prep
%autosetup -p1

%build
%meson  -Dsystemddir=/usr/lib/systemd --buildtype=plain 
%meson_build

%install
%meson_install

%files
%{_bindir}/cpupower-gui
%{_libdir}/cpupower-gui/cpupower-gui-helper
%{_datadir}/applications/org.rnd2.cpupower_gui.desktop
%{_datadir}/cpupower-gui/*
%{_datadir}/dbus-1/services/org.rnd2.cpupower_gui.service
%{_datadir}/dbus-1/system-services/org.rnd2.cpupower_gui.helper.service
%{_datadir}/dbus-1/system.d/org.rnd2.cpupower_gui.helper.conf
%{_datadir}/glib-2.0/schemas/org.rnd2.cpupower_gui.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/org.rnd2.cpupower_gui.svg
%{_datadir}/locale/*
%{_datadir}/metainfo/org.rnd2.cpupower_gui.appdata.xml
%{_datadir}/polkit-1/actions/org.rnd2.cpupower-gui.policy
/var/lib/polkit-1/localauthority/10-vendor.d/org.rnd2.cpupower-gui.pkla
#lib/system/cpupower-gui-helper.service
