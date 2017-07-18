set nocompatible

filetype plugin indent off

set rtp+=~/.vim/bundle/Vundle.vim

"<----PLUGINS---->
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'

Plugin 'nanotech/jellybeans.vim'
Plugin 'altercation/vim-colors-solarized'
Plugin 'vim-scripts/Wombat'
Plugin 'michalbachowski/vim-wombat256mod'
Plugin 'hdima/python-syntax'
Plugin 'Valloric/YouCompleteMe'
Plugin 'jnurmine/Zenburn'
Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'scrooloose/nerdtree'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

call vundle#end()

filetype plugin indent on

"<----COLORS---->
colorscheme jellybeans 
set term=screen-256color
set t_ut=
let g:solarized_termcolors=256
let python_highlight_all=1

"<----TABS---->
set tabstop=4
set softtabstop=4 
set shiftwidth=4
set expandtab

"<----FOLDING---->
set foldmethod=indent
set foldlevel=99
nnoremap <space> za

set laststatus=2
set clipboard=unnamed
