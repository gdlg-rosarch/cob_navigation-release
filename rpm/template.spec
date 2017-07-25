Name:           ros-kinetic-cob-map-accessibility-analysis
Version:        0.6.5
Release:        0%{?dist}
Summary:        ROS cob_map_accessibility_analysis package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_map_accessibility_analysis
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       opencv-devel
Requires:       pcl-devel
Requires:       ros-kinetic-cob-3d-mapping-msgs
Requires:       ros-kinetic-cv-bridge
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
BuildRequires:  boost-devel
BuildRequires:  opencv-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cob-3d-mapping-msgs
BuildRequires:  ros-kinetic-cv-bridge
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf

%description
cob_map_accessibility_analysis receives the map from navigation as well as
obstacles and inflates_obstacles topics to assemble a common obstacle map. Upon
request, this node checks the accessibility of poses within thin map by (i)
checking whether the pose itself is free and by (ii) checking whether there is a
closed path from robot to the goal pose.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Jul 25 2017 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.5-0
- Autogenerated by Bloom

