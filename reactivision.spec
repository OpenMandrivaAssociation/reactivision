%define rname reacTIVision

Summary:	reacTIVision fiducial tracking framework
Name:		reactivision
Version:	1.4
Release:	%mkrel 1
License:	GPL
Group:		Sound
URL:		https://reactivision.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/reactivision/%{rname}-%{version}-src.zip
Source1:	reacTIVision-16x16.png
Source2:	reacTIVision-32x32.png
Source3:	reacTIVision-48x48.png
Patch0:		reactivision-system_portmidi.diff
Requires:	SDL
Requires:	coriander
BuildRequires:	SDL-devel
BuildRequires:	dc1394-devel
BuildRequires:	libalsa-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
reacTIVision is an open source, cross-platform framework for the fast and
robust tracking of fiducial markers. It allows the rapid development of
table-based tangible user interfaces. Its tracking core is using Ross Bencina's
fidtrack library which is basically a newer high-performance implementation of
Enrico Costanza's original d-touch concept.

%prep
%setup -q -n %{rname}-%{version}-src

%build
pushd linux
    %make COPTS="%{optflags}"
popd

%install
rm -rf %{buildroot}

pushd linux
    make DESTDIR=%{buildroot} BINDIR=%{_bindir} PREFIX=%{_prefix} install
popd

mv %{buildroot}%{_bindir}/%{rname} %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{rname}
Comment=reacTIVision fiducial tracking framework
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF

# icons
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

install -m0644 -D %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 -D %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 -D %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{rname}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/*.desktop
