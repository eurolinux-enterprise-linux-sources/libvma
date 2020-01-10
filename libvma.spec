Name: libvma
Version: 8.6.10
Release: 1%{?dist}
Summary: A library for boosting TCP and UDP traffic (over RDMA hardware)

License: GPLv2 or BSD
Url: https://github.com/Mellanox/libvma
# Source: http://github.com/Mellanox/%{name}/archive/%{version}.tar.gz
# Upstream tarballs have no package name in them, locally renaming
Source: %{name}-%{version}.tar.gz
#arm is excluded since libvma fails to compile on arm. 
# utils are only built for x86_64, ppc64/ppc64le, & arm64/aarch64
#Reason: libvma uses assembly commands that are not supported by arm.
ExcludeArch: %{arm} s390 s390x i686 ppc
Requires: pam
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: libmlx5 >= 1.2.1

BuildRequires: librdmacm-devel libibverbs-devel libnl3-devel
BuildRequires: automake autoconf libtool
BuildRequires: libibverbs-devel >= 1.2.1

%description
libvma is a LD_PRELOAD-able library that boosts performance
of TCP and UDP traffic.
It allows application written over standard socket API to handle 
fast path data traffic from user space over Ethernet and/or 
Infiniband with full network stack bypass and get better throughput, 
latency and packets/sec rate.
No application binary change is required for that.
libvma is supported by RDMA capable devices that support
"verbs" IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package devel
Summary: Header files required to develop with libvma 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers files required to develop with the libvma library.

%package utils
Summary: Libvma utilities
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Tools for collecting and analyzing libvma statistic.

%prep
%setup -q

%build
./autogen.sh
%configure 
make %{?_smp_mflags} V=1

%install
%make_install mydoc_DATA=
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# hack to move service file where we want it
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mv $RPM_BUILD_ROOT%{_sysconfdir}/systemd/system/vma.service $RPM_BUILD_ROOT%{_unitdir}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/%{name}*.so.*
#libvma.so in needed in the main package so that 
#'LD_PRELOAD=libvma.so <command>' works.
%{_libdir}/%{name}.so
%{_sysconfdir}/init.d/vma
%{_sbindir}/vmad
%{_unitdir}/vma.service
%license COPYING LICENSE
%doc README.txt journal.txt VMA_VERSION
%config(noreplace) %{_sysconfdir}/libvma.conf
%config(noreplace) %{_sysconfdir}/security/limits.d/30-libvma-limits.conf

%files devel
%{_includedir}/*

%files utils
%{_bindir}/vma_stats

%changelog
* Mon Aug 20 2018 Jarod Wilson <jarod@redhat.com> - 8.6.10-1
- Rebase to upstream v8.6.10 release
- Resolves: rhbz#1613018

* Thu Jun 14 2018 Jarod Wilson <jarod@redhat.com> - 8.5.7-1
- Rebase to upstream v8.5.7 release
- Resolves: rhbz#1541753

* Tue Dec 05 2017 Jarod Wilson <jarod@redhat.com> - 8.4.10-1
- Rebase to upstream v8.4.10 release
- Resolves: rhbz#1456519

* Wed Aug 24 2016 Jarod Wilson <jarod@redhat.com> - 8.1.4-1
- Rebase to 8.1.4 after latest round of coverity fixes upstream
  reduced reported defects to 0
- Related: rhbz#1271624

* Mon Aug 22 2016 Jarod Wilson <jarod@redhat.com> - 8.1.3-1
- Patch in additional coverity fixes from upstream git tree
- Rebase to 8.1.3 to pick up copious coverity corrections
- Related: rhbz#1271624

* Mon Jul 25 2016 Donald Dutile <ddutile@redhat.com> - 8.1.1-1
- Rebase to 8.1.1, re-apply patch to 8.0.1-2
- Add (Build)Requires of libibverbs to 1.2.2
- Resolves: rhbz#1353704

* Wed May 25 2016 Donald Dutile <ddutile@redhat.com> - 8.0.1-2
- ExcludeArch s390's, ppc, i686 and catch in h-file check
- Resolves: rhbz#1271624

* Wed May 25 2016 Donald Dutile <ddutile@redhat.com> - 8.0.1-1
- Initial import to RHEL-7.3
- Resolves: rhbz#1271624

* Sun Mar 13 2016 Alex Vainman <alexv@mellanox.com> - 8.0.1-1
- New upstream release
- Move to dual license: GPLv2 or BSD
- ExcludeArch update
- Removal of extra space in:
  config(noreplace) {_sysconfdir}/security/limits.d/30-libvma-limits.conf
- Add V=1 to make

* Wed Mar  2 2016 Alex Vainman <alexv@mellanox.com> - 7.0.14-2
- Added reasoning for archs exclusion
- Package description improvement
- Removal of the pre scriplet
- Added COPYING and LICENSE files to the package

* Sun Feb 21 2016 Alex Vainman <alexv@mellanox.com> - 7.0.14-1
- New upstream release
- Removal of redundant macros and obsolete/unneeded tags
- Added ExcludeArch, BuildRequires and Require sections
- Fixes and cleanups in the build and installation sections
- Install 30-libvma-limits.conf file under 
  /etc/security/limits.d/
- Fixes related to files/directories ownerships
- Removal of vma_perf_envelope.sh from the utility package
- Update Source tag URL
- Fix most of the rpmlint warnings

* Mon Jan  4 2016 Avner BenHanoch <avnerb@mellanox.com> - 7.0.12-1
- Initial Packaging
