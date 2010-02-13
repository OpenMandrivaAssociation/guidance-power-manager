Name:           guidance-power-manager
Summary:        KDE power management applet
Version:        4.4.0
Release:        %mkrel 1
Url:            http://websvn.kde.org/trunk/extragear/utils/guidance-power-manager
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%{name}-%{version}.tar.bz2
Patch0:		guidance-power-manager-4.4.0-linkage.patch
BuildRequires:  libxscrnsaver-devel
BuildRequires:	libxrandr-devel
BuildRequires:  python-devel
BuildRequires:  python-sip
BuildRequires:  python-dbus
BuildRequires:  python-kde4
BuildRequires:	kdelibs4-devel

Requires:       pm-utils
Requires:       kdebase4-runtime
Requires:       python-kde4
Requires:	    python-dbus

%description
The package provides battery monitoring and suspend/standby triggers.
It is based on the powersave package and therefore supports APM and
ACPI. See powersave package for additional features such as CPU frequency
scaling(SpeedStep and PowerNow) and more

%files -f %name.lang
%defattr(-,root,root) 
%_kde_bindir/guidance-power-manager
%py_platsitedir/ixf86misc.so
%py_platsitedir/xf86misc.py
%_kde_appsdir/guidance-power-manager
%_kde_datadir/autostart/guidance-power-manager.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -fr %buildroot
