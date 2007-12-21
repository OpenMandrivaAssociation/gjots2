%define name	gjots2
%define version 2.3.5
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A note jotter in tree structure
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://bhepple.freeshell.org/gjots/
Source:		http://bhepple.freeshell.org/gjots/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	pygtk2.0-libglade >= 2.2.0
Requires:	openssl
Requires:	gnupg
Requires:	m4
BuildRequires:	ImageMagick
BuildRequires:	python-devel

%description
GJots2 can be used to organize one's jottings into a tree structure,
adding thoughts and miscellaneous things. Afterwards the notes can be
exported into various formats such as HTML, XML, Postscript, PDF, man etc.
It can also make use of OpenSSL, GPG or ccrypt(1) for encrypting PINs
and passwords.

%prep
%setup -q

%install
rm -rf %{buildroot}
python setup.py install --root=%buildroot
%find_lang %name

# menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name} 
Icon=%{name} 
Name=Gjots 
Categories=Office; 
Comment=A simple note jotting utility 
StartupNotify=yes
EOF

# icons
install -d -m 755 %{buildroot}%{_liconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_miconsdir}
convert -geometry 48x48 gjots.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 gjots.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 gjots.png %{buildroot}%{_miconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc %{_docdir}/*
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{py_sitedir}/*
%{_prefix}/lib/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
