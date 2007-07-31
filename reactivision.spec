%define rname reacTIVision

Summary:	reacTIVision fiducial tracking framework
Name:		reactivision
Version:	1.3
Release:	%mkrel 1
License:	GPL
Group:		Sound
URL:		http://www.iua.upf.es/mtg/reacTable/reacTIVision/
Source0:	%{rname}-%{version}.tar.gz
Source1:	reacTIVision-16x16.png
Source2:	reacTIVision-32x32.png
Source3:	reacTIVision-48x48.png
Patch0:		reactivision-system_portmidi.diff
Requires:	SDL
Requires:	coriander
BuildRequires:	gcc-c++
BuildRequires:	SDL-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libdc1394-devel = 1.2.1
BuildRequires:	portmidi-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
reacTIVision is an open source, cross-platform framework for the fast and
robust tracking of fiducial markers. It allows the rapid development of
table-based tangible user interfaces. Its tracking core is using Ross Bencina's
fidtrack library which is basically a newer high-performance implementation of
Enrico Costanza's original d-touch concept.

%prep

%setup -q -n %{rname}-%{version}
%patch0 -p0

cp %{SOURCE1} %{name}-16x16.png
cp %{SOURCE2} %{name}-32x32.png
cp %{SOURCE3} %{name}-48x48.png

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
Categories=GTK;AudioVideo;Audio;AudioVideoEditing;X-MandrivaLinux-Multimedia-Sound;
Encoding=UTF-8
EOF

# icons
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_liconsdir}

install -m0644 %{name}-16x16.png %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 %{name}-32x32.png %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 %{name}-48x48.png %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{rname}/calibration/*.pdf
%{_datadir}/%{rname}/classic/*.png
%{_datadir}/%{rname}/dtouch/*.png
%{_datadir}/%{rname}/*.pdf
%{_datadir}/%{rname}/README.txt
%{_datadir}/%{rname}/LICENSE.txt
%{_datadir}/%{rname}/CHANGELOG.txt
%{_datadir}/%{rname}/GPL.txt
%{_datadir}/%{rname}/midi/README.txt
%{_datadir}/%{rname}/midi/demo.*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/applications/*.desktop
