Name:		cpupower-gui
Version:	0.8.0
Release:	1
License:	GPLv3.0
Summary:	 cpupower-gui is a graphical program that is used to change the scaling frequency limits of the cpu, similar to cpupower. 
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
%meson
%meson_build

%install
%meson_install

%files
#null for now
