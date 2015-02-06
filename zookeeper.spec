%define	major 2
%define libname	%mklibname zookeeper %{major}
%define develname %mklibname zookeeper -d

Summary:	Zookeeper C client library
Name:		zookeeper
Version:	3.4.2
Release:	2
License:	Apache License
Group:		System/Libraries
URL:		http://hadoop.apache.org/zookeeper
Source0:	http://apache.dataphone.se/hadoop/zookeeper/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	http://apache.dataphone.se/hadoop/zookeeper/%{name}-%{version}/%{name}-%{version}.tar.gz.asc
BuildRequires:	autoconf automake libtool
BuildRequires:	cppunit-devel >= 1.10.2
BuildRequires:	dos2unix
BuildRequires:	doxygen
BuildRequires:	graphviz

%description
This package provides a C client interface to Zookeeper server. For general
information about Zookeeper please see %{url}

%package -n	%{libname}
Summary:	Zookeeper C client library
Group:		System/Libraries

%description -n	%{libname}
This package provides a C client interface to Zookeeper server. For general
information about Zookeeper please see %{url}

%package -n	%{develname}
Summary:	Development files for the %{libname} library
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Development files for the %{libname} library.

%prep

%setup -q

%build
pushd src/c
rm -rf autom4te.cache
autoreconf -fis

%configure2_5x \
    --disable-rpath \
    --with-syncapi

%make

make doxygen-doc
popd

%check
pushd src/c
make check
popd

%install
rm -rf %{buildroot}

pushd src/c
%makeinstall_std

# cleanup
rm -f docs/html/*.map
popd

# cleanup
rm -f %{buildroot}%{_libdir}/*.*a

%files
%{_bindir}/cli_mt
%{_bindir}/cli_st
%{_bindir}/load_gen

%files -n %{libname}
%doc src/c/ChangeLog src/c/LICENSE src/c/README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc src/c/docs/html/*
%dir %{_includedir}/zookeeper
%{_includedir}/zookeeper/*.h
%{_libdir}/*.so


%changelog
* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 3.4.2-1
+ Revision: 761289
- 3.4.2
- 3.3.3

* Sat Oct 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3.2.1-1mdv2010.0
+ Revision: 458005
- import zookeeper


* Sat Oct 17 2009 Oden Eriksson <oeriksson@mandriva.com> 3.2.1-1mdv2009.1
- 3.2.1
- the package was renamed to just zookeeper (someone should package the java bits...)

* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdv2009.0
+ Revision: 200092
- import zookeeper-c

* Sat May 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdv2009.0
- initial Mandriva package
