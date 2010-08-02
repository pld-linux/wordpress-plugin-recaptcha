%define		plugin	wp-recaptcha
Summary:	reCAPTCHA support for wordpress
Name:		wordpress-plugin-recaptcha
Version:	2.9.7
Release:	1
License:	MIT
Group:		Applications/Publishing
URL:		http://wordpress.org/extend/plugins/wp-recaptcha/
# Use dropin or something. On each download it has new md5.
# Source0:	http://downloads.wordpress.org/plugin/%{plugin}.%{version}.zip
Source0:	http://execve.pl/PLD/wp-recaptcha.2.9.7.zip
# Source0-md5:	1e1f6004bb69210f9007aafa8ef54788
BuildRequires:	unzip
Requires:	wordpress >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	%{_datadir}/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir		%{wordpressdir}/%{pluginssubdir}
%define		plugindir		%{pluginsdir}/%{plugin}

%description
reCAPTCHA support for wordpress.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a *.php *.png *.css $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{plugindir}
