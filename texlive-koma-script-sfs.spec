# revision 26137
# category Package
# catalog-ctan /macros/latex/contrib/koma-script-SFS
# catalog-date 2008-11-15 10:53:47 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-koma-script-sfs
Version:	1.0
Release:	8
Summary:	Koma-script letter class option for Finnish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/koma-script-SFS
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-sfs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script-sfs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A koma-script parameter set for letters on A4 paper, complying
with Finnish standards SFS 2486, 2487 and 2488; suitable for
window envelopes with window on the left size in the sizes C5,
C65, E5 and E65 (although, because the address window is
smaller, for sizes E5 and E65 the address may not fit within
the window, but ordinary 3-line address should fit).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/koma-script-sfs/SFS.lco
%doc %{_texmfdistdir}/doc/latex/koma-script-sfs/README
%doc %{_texmfdistdir}/doc/latex/koma-script-sfs/SFSesim.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script-sfs/SFSesim.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 813584
- Update to latest release.
- Import texlive-koma-script-sfs
- Import texlive-koma-script-sfs

