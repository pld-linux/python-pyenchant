#
# Conditional build:
%bcond_with	tests	# unit tests (require en_US dictionary)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Spellchecking library for Python 2
Summary(pl.UTF-8):	Biblioteka Pythona 2 sprawdzająca pisownię
Name:		python-pyenchant
Version:	2.0.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyenchant/
Source0:	https://files.pythonhosted.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
# Source0-md5:	c224ea53e119b04116d5301e5027051c
URL:		https://pypi.org/project/pyenchant/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools >= 1:7
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools >= 1:7
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	enchant >= 1.6.0
Requires:	python-libs >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyEnchant is a set of language bindings and some wrapper classes to
make the excellent Enchant spellchecker available as a Python module.

%description -l pl.UTF-8
PyEnchant to zbiór dowiązań języka i klas obudowujących
udostępniających świetną bibliotekę sprawdzania pisowni Enchant jako
moduł Pythona.

%package -n python3-pyenchant
Summary:	Spellchecking library for Python 3
Summary(pl.UTF-8):	Biblioteka Pythona 3 sprawdzająca pisownię
Group:		Libraries/Python
Requires:	enchant >= 1.6.0
Requires:	python3-libs >= 1:3.2

%description -n python3-pyenchant
PyEnchant is a set of language bindings and some wrapper classes to
make the excellent Enchant spellchecker available as a Python module.

%description -n python3-pyenchant -l pl.UTF-8
PyEnchant to zbiór dowiązań języka i klas obudowujących
udostępniających świetną bibliotekę sprawdzania pisowni Enchant jako
moduł Pythona.

%prep
%setup -q -n pyenchant-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/enchant/tests.py*
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/enchant/tests.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/enchant/__pycache__/tests.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.txt TODO.txt
%{py_sitescriptdir}/enchant
%{py_sitescriptdir}/pyenchant-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyenchant
%defattr(644,root,root,755)
%doc README.txt TODO.txt
%{py3_sitescriptdir}/enchant
%{py3_sitescriptdir}/pyenchant-%{version}-py*.egg-info
%endif
