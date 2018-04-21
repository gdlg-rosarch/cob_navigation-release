# Script generated with Bloom
pkgdesc="ROS - This package provides launch files for running <a href="http://ros.org/wiki/care-o-bot">Care-O-bot</a> with the <a href="http://ros.org/wiki/gmapping">gmapping</a> slam package of ROS. It further provides the usual navigation functionalities as provided by the <a href="http://ros.org/wiki/move_base">move_base</a> node."
url='http://ros.org/wiki/cob_navigation_slam'

pkgname='ros-kinetic-cob-navigation-slam'
pkgver='0.6.6_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-supported-robots'
'ros-kinetic-roslaunch'
)

depends=('ros-kinetic-cob-mapping-slam'
'ros-kinetic-cob-navigation-config'
'ros-kinetic-cob-navigation-global'
'ros-kinetic-rviz'
)

conflicts=()
replaces=()

_dir=cob_navigation_slam
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_navigation_slam $srcdir/cob_navigation_slam
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

