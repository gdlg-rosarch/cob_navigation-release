Name:           ros-indigo-cob-navigation-local
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS cob_navigation_local package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_navigation_local
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cob-navigation-config
Requires:       ros-indigo-dwa-local-planner
Requires:       ros-indigo-move-base
Requires:       ros-indigo-rviz
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-supported-robots
BuildRequires:  ros-indigo-roslaunch

%description
This package holds config and launch files for running the move_base node on the
Care-O-bot in an odometric frame. No static map is needed for the move_base node
in this configuration.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 07 2018 Felix Zeltner <fez@ipa.fraunhofer.de> - 0.6.6-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Aug 31 2015 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Matthias Gruhler <mig@ipa.fraunhofer.de> - 0.6.2-0
- Autogenerated by Bloom

