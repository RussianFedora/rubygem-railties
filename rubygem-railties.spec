# Generated from railties-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gemname railties

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global download_path http://rubygems.org/downloads/

%global rubyabi 1.8

Summary: Tools for creating, working with, and running Rails applications
Name: rubygem-%{gemname}
Version: 3.2.13
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://www.rubyonrails.org
Source0: %{download_path}%{gemname}-%{version}.gem
# ** Take LICENSE file from upstream. **
# wget --no-check-certificate https://github.com/rails/rails/raw/master/railties/MIT-LICENSE
Source1: http://github.com/rails/rails/raw/master/railties/MIT-LICENSE
Requires: ruby(abi) = %{rubyabi}
Requires: rubygems
Requires: rubygem(rake) >= 0.8.7
Requires: rubygem(thor) >= 0.14.6
Requires: rubygem(thor) < 2.0
Requires: rubygem(activesupport) = %{version}
Requires: rubygem(actionpack) = %{version}
Requires: rubygem(rdoc) => 3.4
Requires: rubygem(rdoc) < 4
BuildRequires: rubygems
BuildRequires: ruby(abi) = %{rubyabi}
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Rails internals: application bootup, plugins, generators, and rake tasks.
Railties is responsible to glue all frameworks together. Overall, it:
* handles all the bootstrapping process for a Rails application;
* manager rails command line interface;
* provides Rails generators core;

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
%{__mkdir_p} .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --force -V --rdoc %{SOURCE0}
%{__rm} -Rf .%{geminstdir}/.yardoc

# move LICENSE file into place
%{__install} -m 644 %{SOURCE1} .%{geminstdir}/.

# May by only for v.3.0.3-6
#
# Some stylesheet seems to be mistakingly marked as executable in the upstream
# source
find .%{geminstdir} -name *.css -type f -perm /a+x -exec %{__chmod} -v 644 {} \;

%build

%install
%{__mkdir_p} %{buildroot}%{gemdir}
%{__cp} -a .%{gemdir}/* %{buildroot}%{gemdir}

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/guides
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{geminstdir}/CHANGELOG.md
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/MIT-LICENSE
/usr/lib/ruby/gems/%{rubyabi}/bin/rails
/usr/lib/ruby/gems/%{rubyabi}/gems/railties-%{version}/bin/rails

%files doc
%defattr(-, root, root, -)
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Fri Jun 07 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 3.2.13-1
- Update release

* Tue Jul 17 2012 Miroslav Suchý <msuchy@redhat.com> 3.0.10-2
- another round of koji building for rhel 6 (lzap+git@redhat.com)

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.10-1
- Update to Railties 3.0.10

* Thu Jul 21 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-2
- Added missing RDoc dependency.

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to Railties 3.0.9

* Mon Jun 27 2011  <mmorsi@redhat.com> - 3.0.5-2
- include fix for BZ #715385

* Tue Mar 29 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.5-1
- Updated to Railties 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011  <Minnikhanov@gmail.com> - 3.0.3-7
- Fix Comment 11 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c11
- Take LICENSE file from upstream.

* Mon Jan 31 2011  <Minnikhanov@gmail.com> - 3.0.3-6
- Fix Comment 9 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c9
- Temporarily test suite is blocked.

* Thu Jan 27 2011  <Minnikhanov@gmail.com> - 3.0.3-5
- Fix Comment 7 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c7

* Tue Jan 25 2011  <Minnikhanov@gmail.com> - 3.0.3-4
- Fix Comment 5 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c5

* Mon Jan 24 2011  <Minnikhanov@gmail.com> - 3.0.3-3
- Fix Comment 3 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c3

* Sun Jan 23 2011  <Minnikhanov@gmail.com> - 3.0.3-2
- Fix Comment 1 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c1

* Fri Jan 07 2011  <Minnikhanov@gmail.com> - 3.0.3-1
- Initial package
