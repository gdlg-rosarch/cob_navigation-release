# Script generated with Bloom
pkgdesc="ROS - This package holds config and launch files for running the <a href="http://ros.org/wiki/move_base">move_base</a> node on the <a href="http://ros.org/wiki/care-o-bot">Care-O-bot</a>. The move_base node is configured to run over a pre-specified static map."
url='http://ros.org/wiki/cob_navigation_global'

pkgname='ros-kinetic-cob-navigation-global'
pkgver='0.6.6_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-cob-default-env-config'
'ros-kinetic-cob-supported-robots'
'ros-kinetic-roslaunch'
)

depends=('ros-kinetic-amcl'
'ros-kinetic-cob-default-env-config'
'ros-kinetic-cob-linear-nav'
'ros-kinetic-cob-navigation-config'
'ros-kinetic-cob-scan-unifier'
'ros-kinetic-dwa-local-planner'
'ros-kinetic-map-server'
'ros-kinetic-move-base'
'ros-kinetic-rviz'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=cob_navigation_global
source=()
md5sums=()

prepare() {
    cp -R $startdir/cob_navigation_global $srcdir/cob_navigation_global
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

