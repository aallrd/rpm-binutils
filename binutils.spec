Name:           internal-binutils
Version:        2.31
Release:        1%{?dist}
Summary:        The GNU Binutils are a collection of binary tools.
License:        GPL
URL:            https://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

# RPM configuration
#------------------------
# Don't try to auto provide requires
# AutoReqProv:            no
#------------------------

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root
%define _exec_prefix    %{_prefix}
%define _bindir         %{_exec_prefix}/bin
%define _libdir         %{_exec_prefix}/lib
#------------------------

%description
The GNU Binutils are a collection of binary tools.

%prep
%setup -qn binutils-%{version}

%build
./configure --prefix=%{_prefix} --enable-gold=yes --enable-plugins --enable-threads --disable-relro
make tooldir=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
make tooldir=$RPM_BUILD_ROOT/%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/ar
%{_bindir}/as
%{_bindir}/ld
%{_bindir}/ld.bfd
%{_bindir}/ld.gold
%{_bindir}/nm
%{_bindir}/objcopy
%{_bindir}/objdump
%{_bindir}/ranlib
%{_bindir}/readelf
%{_bindir}/strip
%{_libdir}/ldscripts/elf32_x86_64.x
%{_libdir}/ldscripts/elf32_x86_64.xbn
%{_libdir}/ldscripts/elf32_x86_64.xc
%{_libdir}/ldscripts/elf32_x86_64.xce
%{_libdir}/ldscripts/elf32_x86_64.xd
%{_libdir}/ldscripts/elf32_x86_64.xdc
%{_libdir}/ldscripts/elf32_x86_64.xdce
%{_libdir}/ldscripts/elf32_x86_64.xde
%{_libdir}/ldscripts/elf32_x86_64.xdw
%{_libdir}/ldscripts/elf32_x86_64.xdwe
%{_libdir}/ldscripts/elf32_x86_64.xe
%{_libdir}/ldscripts/elf32_x86_64.xn
%{_libdir}/ldscripts/elf32_x86_64.xr
%{_libdir}/ldscripts/elf32_x86_64.xs
%{_libdir}/ldscripts/elf32_x86_64.xsc
%{_libdir}/ldscripts/elf32_x86_64.xsce
%{_libdir}/ldscripts/elf32_x86_64.xse
%{_libdir}/ldscripts/elf32_x86_64.xsw
%{_libdir}/ldscripts/elf32_x86_64.xswe
%{_libdir}/ldscripts/elf32_x86_64.xu
%{_libdir}/ldscripts/elf32_x86_64.xw
%{_libdir}/ldscripts/elf32_x86_64.xwe
%{_libdir}/ldscripts/elf_i386.x
%{_libdir}/ldscripts/elf_i386.xbn
%{_libdir}/ldscripts/elf_i386.xc
%{_libdir}/ldscripts/elf_i386.xce
%{_libdir}/ldscripts/elf_i386.xd
%{_libdir}/ldscripts/elf_i386.xdc
%{_libdir}/ldscripts/elf_i386.xdce
%{_libdir}/ldscripts/elf_i386.xde
%{_libdir}/ldscripts/elf_i386.xdw
%{_libdir}/ldscripts/elf_i386.xdwe
%{_libdir}/ldscripts/elf_i386.xe
%{_libdir}/ldscripts/elf_i386.xn
%{_libdir}/ldscripts/elf_i386.xr
%{_libdir}/ldscripts/elf_i386.xs
%{_libdir}/ldscripts/elf_i386.xsc
%{_libdir}/ldscripts/elf_i386.xsce
%{_libdir}/ldscripts/elf_i386.xse
%{_libdir}/ldscripts/elf_i386.xsw
%{_libdir}/ldscripts/elf_i386.xswe
%{_libdir}/ldscripts/elf_i386.xu
%{_libdir}/ldscripts/elf_i386.xw
%{_libdir}/ldscripts/elf_i386.xwe
%{_libdir}/ldscripts/elf_iamcu.x
%{_libdir}/ldscripts/elf_iamcu.xbn
%{_libdir}/ldscripts/elf_iamcu.xc
%{_libdir}/ldscripts/elf_iamcu.xce
%{_libdir}/ldscripts/elf_iamcu.xd
%{_libdir}/ldscripts/elf_iamcu.xdc
%{_libdir}/ldscripts/elf_iamcu.xdce
%{_libdir}/ldscripts/elf_iamcu.xde
%{_libdir}/ldscripts/elf_iamcu.xdw
%{_libdir}/ldscripts/elf_iamcu.xdwe
%{_libdir}/ldscripts/elf_iamcu.xe
%{_libdir}/ldscripts/elf_iamcu.xn
%{_libdir}/ldscripts/elf_iamcu.xr
%{_libdir}/ldscripts/elf_iamcu.xs
%{_libdir}/ldscripts/elf_iamcu.xsc
%{_libdir}/ldscripts/elf_iamcu.xsce
%{_libdir}/ldscripts/elf_iamcu.xse
%{_libdir}/ldscripts/elf_iamcu.xsw
%{_libdir}/ldscripts/elf_iamcu.xswe
%{_libdir}/ldscripts/elf_iamcu.xu
%{_libdir}/ldscripts/elf_iamcu.xw
%{_libdir}/ldscripts/elf_iamcu.xwe
%{_libdir}/ldscripts/elf_k1om.x
%{_libdir}/ldscripts/elf_k1om.xbn
%{_libdir}/ldscripts/elf_k1om.xc
%{_libdir}/ldscripts/elf_k1om.xce
%{_libdir}/ldscripts/elf_k1om.xd
%{_libdir}/ldscripts/elf_k1om.xdc
%{_libdir}/ldscripts/elf_k1om.xdce
%{_libdir}/ldscripts/elf_k1om.xde
%{_libdir}/ldscripts/elf_k1om.xdw
%{_libdir}/ldscripts/elf_k1om.xdwe
%{_libdir}/ldscripts/elf_k1om.xe
%{_libdir}/ldscripts/elf_k1om.xn
%{_libdir}/ldscripts/elf_k1om.xr
%{_libdir}/ldscripts/elf_k1om.xs
%{_libdir}/ldscripts/elf_k1om.xsc
%{_libdir}/ldscripts/elf_k1om.xsce
%{_libdir}/ldscripts/elf_k1om.xse
%{_libdir}/ldscripts/elf_k1om.xsw
%{_libdir}/ldscripts/elf_k1om.xswe
%{_libdir}/ldscripts/elf_k1om.xu
%{_libdir}/ldscripts/elf_k1om.xw
%{_libdir}/ldscripts/elf_k1om.xwe
%{_libdir}/ldscripts/elf_l1om.x
%{_libdir}/ldscripts/elf_l1om.xbn
%{_libdir}/ldscripts/elf_l1om.xc
%{_libdir}/ldscripts/elf_l1om.xce
%{_libdir}/ldscripts/elf_l1om.xd
%{_libdir}/ldscripts/elf_l1om.xdc
%{_libdir}/ldscripts/elf_l1om.xdce
%{_libdir}/ldscripts/elf_l1om.xde
%{_libdir}/ldscripts/elf_l1om.xdw
%{_libdir}/ldscripts/elf_l1om.xdwe
%{_libdir}/ldscripts/elf_l1om.xe
%{_libdir}/ldscripts/elf_l1om.xn
%{_libdir}/ldscripts/elf_l1om.xr
%{_libdir}/ldscripts/elf_l1om.xs
%{_libdir}/ldscripts/elf_l1om.xsc
%{_libdir}/ldscripts/elf_l1om.xsce
%{_libdir}/ldscripts/elf_l1om.xse
%{_libdir}/ldscripts/elf_l1om.xsw
%{_libdir}/ldscripts/elf_l1om.xswe
%{_libdir}/ldscripts/elf_l1om.xu
%{_libdir}/ldscripts/elf_l1om.xw
%{_libdir}/ldscripts/elf_l1om.xwe
%{_libdir}/ldscripts/elf_x86_64.x
%{_libdir}/ldscripts/elf_x86_64.xbn
%{_libdir}/ldscripts/elf_x86_64.xc
%{_libdir}/ldscripts/elf_x86_64.xce
%{_libdir}/ldscripts/elf_x86_64.xd
%{_libdir}/ldscripts/elf_x86_64.xdc
%{_libdir}/ldscripts/elf_x86_64.xdce
%{_libdir}/ldscripts/elf_x86_64.xde
%{_libdir}/ldscripts/elf_x86_64.xdw
%{_libdir}/ldscripts/elf_x86_64.xdwe
%{_libdir}/ldscripts/elf_x86_64.xe
%{_libdir}/ldscripts/elf_x86_64.xn
%{_libdir}/ldscripts/elf_x86_64.xr
%{_libdir}/ldscripts/elf_x86_64.xs
%{_libdir}/ldscripts/elf_x86_64.xsc
%{_libdir}/ldscripts/elf_x86_64.xsce
%{_libdir}/ldscripts/elf_x86_64.xse
%{_libdir}/ldscripts/elf_x86_64.xsw
%{_libdir}/ldscripts/elf_x86_64.xswe
%{_libdir}/ldscripts/elf_x86_64.xu
%{_libdir}/ldscripts/elf_x86_64.xw
%{_libdir}/ldscripts/elf_x86_64.xwe

# Directories owned by this RPM
%dir %{_libdir}/ldscripts

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Created the RPM package
