# rpm-internal-binutils

Build aRPM package for the **internal-binutils** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: internal-binutils.spec
[...]
[SUCCESS] [18:06:18] Binary RPM file(s):
[SUCCESS] [18:06:18] * /root/rpmbuild/RPMS/x86_64/internal-binutils-2.31-1.el6.x86_64.rpm
[SUCCESS] [18:06:18] * /root/rpmbuild/RPMS/x86_64/internal-binutils-debuginfo-2.31-1.el6.x86_64.rpm
[SUCCESS] [18:06:18] Source RPM file(s):
[SUCCESS] [18:06:18] * /root/rpmbuild/SRPMS/internal-binutils-2.31-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure thevendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF
```

# Install the package using Yum
```
$ yum install -y --disablerepo=* --enablerepo=vendor-internal internal-binutils
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-binutils-2.31-1.el6.x86_64.rpm
$ rpm -ivh internal-binutils-2.31-1.el6.x86_64.rpm
Preparing...         ########################################### [100%]
   1:internal-binutils  ########################################### [100%]
```

## Usage

```
$ export PATH=/opt/internal/root/bin:${PATH}
$ ld.gold --version
GNU gold (GNU Binutils 2.31) 1.16
Copyright (C) 2018 Free Software Foundation, Inc.
This program is free software; you may redistribute it under the terms of
the GNU General Public License version 3 or (at your option) a later version.
This program has absolutely no warranty.
```
