%define		pname pyenchant
Summary:	Spellchecking library for Python
Summary(pl.UTF-8):	Biblioteka Pythona sprawdzająca pisownię
Name:		python-%{pname}
Version:	1.5.3
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pyenchant/%{pname}-%{version}.tar.gz
# Source0-md5:	d327fb9c8620ecc261a424083dc9aa95
Patch0:		%{name}-ez_setup.patch
URL:		http://pyenchant.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	enchant-devel >= 1.3.0
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.c3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	enchant >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyEnchant is a set of language bindings and some wrapper classes to
make the excellent Enchant spellchecker available as a Python module.

%description -l pl.UTF-8
PyEnchant to zbiór dowiązań języka i klas obudowujących
udostępniających świetną bibliotekę sprawdzania pisowni Enchant jako
moduł Pythona.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--root $RPM_BUILD_ROOT \
	--single-version-externally-managed

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt TODO.txt
%dir %{py_sitescriptdir}/enchant
%{py_sitescriptdir}/enchant/*.py[co]
%dir %{py_sitescriptdir}/enchant/checker
%{py_sitescriptdir}/enchant/checker/*.py[co]
%dir %{py_sitescriptdir}/enchant/tokenize
%{py_sitescriptdir}/enchant/tokenize/*.py[co]
%{py_sitescriptdir}/pyenchant-%{version}-py*.egg-info
