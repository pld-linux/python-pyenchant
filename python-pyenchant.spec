%define		pname pyenchant
Summary:	Spellchecking library for Python
Summary(pl.UTF-8):	Biblioteka Pythona sprawdzająca pisownię
Name:		python-%{pname}
Version:	1.3.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/pyenchant/%{pname}-%{version}.tar.gz
# Source0-md5:	3b069a14a985bd71759560a03bbb8bd3
URL:		http://pyenchant.sourceforge.net/
BuildRequires:	enchant-devel >= 1.3.0
BuildRequires:	python-devel
BuildRequires:	python-setuptools
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--single-version-externally-managed

find $RPM_BUILD_ROOT%{py_sitedir}/enchant -name '*.py' -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{pname}-%{version}-*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt TODO.txt
%dir %{py_sitedir}/enchant
%dir %{py_sitedir}/enchant/checker
%dir %{py_sitedir}/enchant/tokenize
%attr(755,root,root) %{py_sitedir}/enchant/*.so
%{py_sitedir}/enchant/*.py[oc]
%{py_sitedir}/enchant/checker/*.py[oc]
%{py_sitedir}/enchant/tokenize/*.py[oc]
