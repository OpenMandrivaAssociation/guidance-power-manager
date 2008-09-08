Name:           guidance-power-manager
Summary:        KDE power management applet
Version:        4.1.1
Release:        %mkrel 2
Url:            http://websvn.kde.org/trunk/extragear/utils/guidance-power-manager
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/%version/src/extragear/%{name}-%{version}.tar.bz2

BuildRequires:  kdebase4-workspace-devel
BuildRequires:  automoc
BuildRequires:  libxscrnsaver-devel
BuildRequires:  python-devel
BuildRequires:  python-sip
BuildRequires:  python-dbus
BuildRequires:  python-kde4

Requires:       pm-utils
Requires:       kdebase4-runtime
Requires:       python-kde4
Requires:	python-dbus

%description
The package provides battery monitoring and suspend/standby triggers.
It is based on the powersave package and therefore supports APM and
ACPI. See powersave package for additional features such as CPU frequency
scaling(SpeedStep and PowerNow) and more

%files
%defattr(-,root,root) 
#-f %name.lang
%_kde_bindir/guidance-power-manager
%py_platsitedir/ixf86misc.so
%py_platsitedir/xf86misc.py
%_kde_appsdir/guidance-power-manager
%_kde_datadir/autostart/guidance-power-manager.desktop
%_kde_datadir/locale/*/LC_MESSAGES/*.mo

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
pushd build
make DESTDIR=%buildroot install
popd

# FIXME
#%find_lang %{name} --with-html

%clean
%{__rm} -rf "%{buildroot}"
