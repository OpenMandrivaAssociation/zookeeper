%define	major 2
%define libname	%mklibname zookeeper %{major}
%define develname %mklibname zookeeper -d

Summary:	Zookeeper C client library
Name:		zookeeper
Version:	3.3.3
Release:	%mkrel 1
License:	Apache License
Group:		System/Libraries
URL:		http://hadoop.apache.org/zookeeper
Source0:	http://apache.dataphone.se/hadoop/zookeeper/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:	http://apache.dataphone.se/hadoop/zookeeper/%{name}-%{version}/%{name}-%{version}.tar.gz.asc
BuildRequires:	cppunit-devel >= 1.10.2
BuildRequires:	dos2unix
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cli_mt
%{_bindir}/cli_st
%{_bindir}/load_gen

%files -n %{libname}
%defattr(-,root,root)
%doc src/c/ChangeLog src/c/LICENSE src/c/README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc src/c/docs/html/*
%dir %{_includedir}/c-client-src
%{_includedir}/c-client-src/*.h
%{_libdir}/*.so
%{_libdir}/*.*a

