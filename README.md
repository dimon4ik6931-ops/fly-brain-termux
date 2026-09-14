# Emulation of the *Drosophila Fly* Brain

Для этого скрипта требуется наличие root

Инструкция по установке:

$pkg update && pkg upgrade 

pkg install python pip git 

pip install Jinja2 pytorch numpy pillow sympy

git clone https://github.com/dimon4ik6931-ops/fly-brain-termux.git

cd fly-brain-termux

python main.py --pytorch --t_run 600 --n_run 1 --no_log_file

--pytorch для использования pytorch

--t_tun и время в секундах

--no_log_file отключает лишние логи

Изменения 15 сен 2026: 

Улучшен интеллект и добавлена долговременная память с автоматическим сохранением. 
