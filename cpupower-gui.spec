%global debug_package %{nil}
%define _userunitdir /lib/systemd/

Name:		cpupower-gui
Version:	1.0.0
Release:	3
License:	GPLv3.0
Summary:	cpupower-gui is a graphical program that is used to change the scaling frequency limits of the cpu, similar to cpupower. 
URL:		https://github.com/vagnum08/cpupower-gui
Group:		System/Kernel and hardware
Source0:	https://github.com/vagnum08/cpupower-gui/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  gettext-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  python3dist(pyxdg)

Requires:   python
Requires:   gtk+3
Requires:   python-dbus
Requires:   python3dist(pygobject)
Requires:   python3dist(pyxdg)
Requires:   hicolor-icon-theme
Requires:   polkit
Requires:   lib64handy-gir1
%description
This program is designed to allow you to change the frequency limits of your cpu and its governor. The application is similar in functionality to cpupower but use GTK GUI and CLI.

%prep
%autosetup -p1
sed -i '15d' %{_builddir}/%{name}-%{version}/data/meson.build

%build
%meson  -Dsystemddir=/lib/systemd --buildtype=plain 
%meson_build

%install
%meson_install
rm -rf  %{buildroot}/var/lib/polkit-1/localauthority/10-vendor.d/org.rnd2.cpupower-gui.pkla

%files
%{_bindir}/cpupower-gui
%{_libdir}/cpupower-gui/cpupower-gui-helper
%{_sysconfdir}/cpupower_gui.conf
%{_sysconfdir}/cpupower_gui.d/README
%{_sysconfdir}/cpupower_gui.d/my_profile.profile.ex
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
%{_datadir}/polkit-1/rules.d/org.rnd2.cpupower-gui.rules
%{_userunitdir}/system/cpupower-gui-helper.service
%{_userunitdir}/system/cpupower-gui.service
%{_prefix}/lib/systemd/user/cpupower-gui-user.service

%post
systemctl enable cpupower-gui-helper 

%preun 
systemctl disable cpupower-gui-helper cpupower-gui