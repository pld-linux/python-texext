#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extensions for working with LaTeX math
Summary(pl.UTF-8):	Rozszerzenia Sphinksa do pracy z LaTeXowymi wzorami matematycznymi
Name:		python-texext
Version:	0.6.5
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/texext/
Source0:	https://files.pythonhosted.org/packages/source/t/texext/texext-%{version}.tar.gz
# Source0-md5:	4f86a0cd2e75f1779b713b8342c7cdc6
URL:		https://pypi.org/project/texext/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.3.1
BuildRequires:	python-docutils >= 0.12
BuildRequires:	python-matplotlib >= 1.4.3
BuildRequires:	python-pytest
BuildRequires:	python-six >= 1.4.0
BuildRequires:	python-sphinxtesters >= 0.2
BuildRequires:	python-sympy >= 0.7
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.3.1
BuildRequires:	python3-docutils >= 0.12
BuildRequires:	python3-matplotlib >= 1.4.3
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.4.0
BuildRequires:	python3-sphinxtesters >= 0.2
BuildRequires:	python3-sympy >= 0.7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
texext contains a couple of Sphinx extensions for working with LaTeX
math.

%description -l pl.UTF-8
texext zawiera kilka rozszerzeń Sphinksa do pracy z LaTeXowymi wzorami
matematycznymi.

%package -n python3-texext
Summary:	Sphinx extensions for working with LaTeX math
Summary(pl.UTF-8):	Rozszerzenia Sphinksa do pracy z LaTeXowymi wzorami matematycznymi
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-texext
texext contains a couple of Sphinx extensions for working with LaTeX
math.

%description -n python3-texext -l pl.UTF-8
texext zawiera kilka rozszerzeń Sphinksa do pracy z LaTeXowymi wzorami
matematycznymi.

%prep
%setup -q -n texext-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest texext/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python3} -m pytest texext/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/texext
%{py_sitescriptdir}/texext-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-texext
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/texext
%{py3_sitescriptdir}/texext-%{version}-py*.egg-info
%endif
