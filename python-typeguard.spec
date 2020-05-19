%global pypi_name typeguard

Name:           python-%{pypi_name}
Version:        2.7.1
Release:        1%{?dist}
Summary:        Run-time type checker for Python
License:        MIT
URL:            https://github.com/agronholm/%{pypi_name}
Source0:        https://pypi.io/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python3-%{pypi_name}

Summary:          %{common_desc}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:    python3-setuptools
BuildRequires:    python3-setuptools_scm
BuildRequires:    python3-devel
BuildRequires:    python3-pbr
BuildRequires:    python3-six >= 1.9.0
BuildRequires:    python3-tornado >= 4.5
BuildRequires:    python3-pytest
BuildRequires:    python3-pytest-cov
%if %{undefined __pythondist_requires}
Requires:         python3-six >= 1.9.0
%endif


%description -n python3-%{pypi_name}
This library provides run-time type checking for functions defined with PEP
484 argument (and return) type annotations.

%description
This library provides run-time type checking for functions defined with PEP
484 argument (and return) type annotations.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Wed May 6 2020 Christopher Brown <chris.brown@redhat.com> - 2.7.1-1
- Initial package at 2.7.1
