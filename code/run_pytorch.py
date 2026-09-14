import os
import time
import torch
import random
import string
import subprocess

# ==============================================================================
#                 🛠️ АДАПТИВНОЕ ОПРЕДЕЛЕНИЕ РАЗМЕРОВ ЭКРАНА
# ==============================================================================
def get_screen_resolution():
    """Получает реальное разрешение экрана через ADB/Root, учитывая ориентацию"""
    try:
        output = subprocess.check_output('su -c "wm size"', shell=True).decode('utf-8')
        res_str = output.strip().split()[-1]
        w, h = map(int, res_str.split('x'))
        return w, h
    except Exception:
        return 1080, 2400

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_resolution()

# ==============================================================================
#                 🧪 ПОЛНЫЙ ДИНАМИЧЕСКИЙ НЕЙРОХИМИЧЕСКИЙ ПУЛ
# ==============================================================================
class NeurochemistryPool:
    """
    Модуль полной биохимии мозга.
    Все медиаторы имеют базовый уровень (baseline), скорость расщепления (decay)
    и текущую концентрацию (levels).
    """
    def __init__(self):
        self.levels = {
            "dopamine": 1.0,         # Дофамин: Обучение / Награда
            "octopamine": 0.2,        # Октопамин/Норадреналин: Стресс / Ошибки
            "serotonin": 0.5,         # Серотонин: Спокойствие / Торможение
            "acetylcholine": 3.5,    # Ацетилхолин: Внимание / Проводимость
            "gaba": 0.5,              # ГАМК: Жесткое торможение / Реполяризация
            "glutamate": 3.0,         # Глутамат: Возбуждение / Входной сигнал
            "endocannabinoids": 0.1,  # Эндоканнабиноиды: Защита от перегруза
            "stress_crh": 0.0,        # Кортиколиберин: Паника / Хаос
            "npy": 0.5,               # Нейропептид Y: Антистресс / Гомеостаз
            "oxytocin": 0.5,          # Окситоцин: Стабилизация связей
            "histamine": 1.0          # Гистамин: Тонус бодрствования
        }

        self.decay = {
            "dopamine": 0.5,
            "octopamine": 0.2,
            "serotonin": 0.02,
            "acetylcholine": 0.03,
            "gaba": 0.1,
            "glutamate": 0.05,
            "endocannabinoids": 0.15,
            "stress_crh": 0.01,
            "npy": 0.02,
            "oxytocin": 0.01,
            "histamine": 0.04
        }

        self.baseline = {
            "dopamine": 0.5,
            "octopamine": 0.2,
            "serotonin": 0.5,
            "acetylcholine": 1.0,
            "gaba": 0.5,
            "glutamate": 1.0,
            "endocannabinoids": 0.0,
            "stress_crh": 0.0,
            "npy": 0.5,
            "oxytocin": 0.5,
            "histamine": 1.0
        }

    def update_homeostasis(self):
        """Ежешаговый процесс ферментативного расщепления и возврата к норме"""
        for neuro in self.levels:
            delta = (self.baseline[neuro] - self.levels[neuro]) * self.decay[neuro]
            self.levels[neuro] += delta

    def inject(self, name, amount):
        """Всплеск или падение концентрации медиатора"""
        if name in self.levels:
            self.levels[name] = max(0.0, self.levels[name] + amount)

    def set_level(self, name, value):
        """Ручная принудительная установка уровня (для тестов/стимуляции)"""
        if name in self.levels:
            self.levels[name] = max(0.0, float(value))


# ==============================================================================
#                 🎛️ БИОФИЗИЧЕСКАЯ КОНФИГУРАЦИЯ НЕЙРОНОВ (LIF MODEL)
# ==============================================================================
CONFIG = {
    # 📱 ГЕОМЕТРИЯ ЭКРАНА И ПРОСТРАНСТВО ЦЕЛЕЙ (динамически адаптируются под ориентацию)
    "MAX_X": SCREEN_WIDTH,       # Максимальное разрешение экрана по оси X (Ширина в пикселях)
    "MAX_Y": SCREEN_HEIGHT,      # Максимальное разрешение экрана по оси Y (Высота в пикселях)
    "TARGET_RADIUS": int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.35), 
                                 # Радиус целевой зоны (в пикселях от центра), в которой действие
                                 # считается успешным и вызывает дофаминовое подкрепление

    # 🔬 БАЗОВАЯ ФИЗИКА И ЭЛЕКТРОФИЗИОЛОГИЯ КЛЕТОК (Leaky Integrate-and-Fire)
    "N_NEURONS": 2000,           # Общее количество симулируемых нейронов в нейронной сети
    "V_REST_BASE": -70.0,        # Базовый потенциал покоя мембраны (мВ). Уровень, к которому
                                 # стремится клетка при отсутствии внешних токов
    "V_THRESH_BASE": -50.0,      # Базовый порог генерации спайка (мВ). При достижении этого напряжения
                                 # нейрон "взрывается" и посылает сигнал далее по синапсам
    "V_RESET": -65.0,            # Потенциал сброса (мВ). Напряжение, до которого мгновенно
                                 # опускается мембрана сразу после испускания спайка (рефрактерная фаза)
    
    # ⏳ ДИНАМИКА ПАМЯТИ И ПРОВОДИМОСТИ
    "BASE_DECAY": 0.85,          # Базовый коэффициент утечки заряда (0.0 — мгновенный сброс, 1.0 — заряд не гаснет).
                                 # Определяет кратковременную память нейрона между шагами времени
    "BASE_SYNAPSE_WEIGHT": 100.0,  # Начальный вес (сила) случайных синаптических связей при создании сети
}


# ==============================================================================
#                 🕹️ ПОЛНЫЙ МОТОРНЫЙ ЦЕНТР (ANDROID OS)
# ==============================================================================
def execute_fly_action(action_type, tx, ty, extra_param=None):
    max_x = CONFIG["MAX_X"]
    max_y = CONFIG["MAX_Y"]
    
    tx = max(30, min(tx, max_x - 30))
    ty = max(30, min(ty, max_y - 30))

    if action_type == 0:
        os.system(f'su -c "input tap {tx} {ty}"')
        return f"👆 [TAP] Клик в ({tx}, {ty})"
    elif action_type == 1:
        os.system(f'su -c "input swipe {tx} {ty} {tx} {ty} 800"')
        return f"🖐️ [LONG PRESS] Зажатие в ({tx}, {ty})"
    elif action_type == 2:
        start_y = int(max_y * 0.7)
        end_y = int(max_y * 0.2)
        os.system(f'su -c "input swipe {tx} {start_y} {tx} {end_y} 300"')
        return f"📜 [SCROLL DOWN] Скролл вниз по X={tx}"
    elif action_type == 3:
        start_y = int(max_y * 0.2)
        end_y = int(max_y * 0.7)
        os.system(f'su -c "input swipe {tx} {start_y} {tx} {end_y} 300"')
        return f"📜 [SCROLL UP] Скролл вверх по X={tx}"
    elif action_type == 4:
        os.system('su -c "input keyevent 4"')
        return "◀️ [SYSTEM] Кнопка 'Назад'"
    elif action_type == 5:
        os.system('su -c "input keyevent 3"')
        return "🏠 [SYSTEM] Кнопка 'Домой'"
    elif action_type == 6:
        text_to_type = extra_param or "".join(random.choices(string.ascii_lowercase, k=5))
        os.system(f'su -c "input text {text_to_type}"')
        return f"⌨️ [KEYBOARD] Ввод: '{text_to_type}'"
    elif action_type == 7:
        os.system('su -c "input keyevent 187"')
        return "📱 [SYSTEM] Меню недавних"
    else:
        return f"⛔ Мозг мухи запущен с вашими настройками"


# ==============================================================================
#                 🧠 СИМУЛЯЦИЯ МОЗГА С УПРАВЛЯЕМОЙ ХИМИЕЙ
# ==============================================================================
def run_all_benchmarks(**kwargs):
    logger = kwargs.get('logger')
    t_run_values = kwargs.get('t_run_values', [600.0])
    
    cx, cy = CONFIG["MAX_X"] // 2, CONFIG["MAX_Y"] // 2

    chem = NeurochemistryPool()
    voltages = torch.ones(CONFIG["N_NEURONS"]) * CONFIG["V_REST_BASE"]
    synapses = torch.randn(CONFIG["N_NEURONS"], CONFIG["N_NEURONS"]) * CONFIG["BASE_SYNAPSE_WEIGHT"]

    for t_run in t_run_values:
        steps = int(t_run * 1000)

        for step in range(steps):
            # 1. Динамическая физика мембран на основе нейрохимии
            v_rest_dynamic = CONFIG["V_REST_BASE"] - (chem.levels["gaba"] * 10.0)
            v_thresh_dynamic = CONFIG["V_THRESH_BASE"] + (chem.levels["serotonin"] * 8.0)
            effective_synapses = synapses * chem.levels["acetylcholine"]
            
            noise_amplitude = (7.5 * chem.levels["glutamate"] * chem.levels["histamine"]) 
            noise_amplitude += (chem.levels["stress_crh"] * 15.0)

            # 2. Вычисление токов
            stimulus = torch.randn(CONFIG["N_NEURONS"]) * noise_amplitude
            if chem.levels["endocannabinoids"] > 0.5:
                stimulus *= 0.3

            voltages += stimulus
            spikes = voltages >= v_thresh_dynamic
            num_spikes = torch.sum(spikes).item()

            if num_spikes > 0:
                voltages[spikes] = CONFIG["V_RESET"]

                if num_spikes > 50:
                    chem.inject("endocannabinoids", 0.4)

                # 3. Декодирование активности в моторные команды
                if num_spikes > 4:
                    act_val = torch.mean(voltages[0:50]).item()
                    x_val = torch.mean(voltages[50:150]).item()
                    y_val = torch.mean(voltages[150:250]).item()

                    action_type = int(abs(act_val) * 100) % 8
                    rx = int(abs(x_val) * 50) % CONFIG["MAX_X"]
                    ry = int(abs(y_val) * 80) % CONFIG["MAX_Y"]

                    action_desc = execute_fly_action(action_type, rx, ry)
                    dist = ((rx - cx)**2 + (ry - cy)**2)**0.5
                    spikes_matrix = spikes.float().unsqueeze(0)

                    # 4. Модификация связей (STDP) и биохимическая реакция
                    if dist <= CONFIG["TARGET_RADIUS"]:
                        chem.inject("dopamine", 10.0)
                        chem.inject("oxytocin", 1.5)
                        chem.inject("stress_crh", -1.0)
                        
                        learning_rate = 1.0 / (0.5 + chem.levels["oxytocin"])
                        synapses += learning_rate * chem.levels["dopamine"] * torch.mm(spikes_matrix.t(), spikes_matrix)
                        voltages += (chem.levels["dopamine"] * 2.0)

                        if logger:
                            logger.log(f"🟢 [ПОДКРЕПЛЕНИЕ]: {action_desc} | Дофамин: {chem.levels['dopamine']:.2f}")
                    else:
                        chem.inject("octopamine", 1.0)
                        chem.inject("stress_crh", 0.5)
                        chem.inject("dopamine", -2.0)

                        synapses -= chem.levels["octopamine"] * torch.mm(spikes_matrix.t(), spikes_matrix)

                        if logger:
                            logger.log(f"🔴 [ОШИБКА]: {action_desc} | Октопамин: {chem.levels['octopamine']:.2f} | CRH: {chem.levels['stress_crh']:.2f}")

            # 5. Возврат к гомеостазу
            voltages = v_rest_dynamic + (voltages - v_rest_dynamic) * CONFIG["BASE_DECAY"]
            chem.update_homeostasis()

    return {}
