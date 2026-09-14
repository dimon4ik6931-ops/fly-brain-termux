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
            "acetylcholine": 5.0,    # Ацетилхолин: Внимание / Проводимость (усилено для фокуса)
            "gaba": 1.5,              # ГАМК: Жесткое торможение / Реполяризация (повышено для стабильности)
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
            "gaba": 1.5,
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
#                 🎛️ БИОФИЗИЧЕСКАЯ КОНФИГУРАЦИЯ НЕЙРОНОВ И ПАМЯТИ
# ==============================================================================
CONFIG = {
    # 📱 ГЕОМЕТРИЯ ЭКРАНА И ПРОСТРАНСТВО ЦЕЛЕЙ
    "MAX_X": SCREEN_WIDTH,       
    "MAX_Y": SCREEN_HEIGHT,      
    "TARGET_RADIUS": int(min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.35), 

    # 🔬 БАЗОВАЯ ФИЗИКА И ЭЛЕКТРОФИЗИОЛОГИЯ КЛЕТОК
    "N_NEURONS": 2000,           
    "V_REST_BASE": -70.0,        
    "V_THRESH_BASE": -50.0,      
    "V_RESET": -65.0,            
    
    # ⏳ ДИНАМИКА ПАМЯТИ И ПРОВОДИМОСТИ
    "BASE_DECAY": 0.85,          
    "BASE_SYNAPSE_WEIGHT": 350.0,  

    # 💾 НАСТРОЙКИ СОХРАНЕНИЯ ОПЫТА И АВТОБЭКАПА
    "RESUME_TRAINING": True,
    "CHECKPOINT_PATH": "data/results/learned_brain_synapses.pt",
    "AUTOSAVE_INTERVAL_SEC": 15.0
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
#                                🧠 СИМУЛЯЦИЯ МОЗГА
# ==============================================================================
def run_all_benchmarks(**kwargs):
    logger = kwargs.get('logger')
    t_run_values = kwargs.get('t_run_values', [600.0])
    
    cx, cy = CONFIG["MAX_X"] // 2, CONFIG["MAX_Y"] // 2

    chem = NeurochemistryPool()
    voltages = torch.ones(CONFIG["N_NEURONS"]) * CONFIG["V_REST_BASE"]

    # 📦 ЗАГРУЗКА ИЛИ СОЗДАНИЕ ПАМЯТИ (ВЕСОВ И ПОРОГОВ)
    if CONFIG["RESUME_TRAINING"] and os.path.exists(CONFIG["CHECKPOINT_PATH"]):
        print(f"📦 Загрузка памяти мозга из: {CONFIG['CHECKPOINT_PATH']}")
        checkpoint = torch.load(CONFIG["CHECKPOINT_PATH"])
        synapses = checkpoint["synapses"]
        v_thresholds = checkpoint["v_thresholds"]
    else:
        print("🧠 Создание новой матрицы синапсов и порогов с нуля...")
        synapses = torch.randn(CONFIG["N_NEURONS"], CONFIG["N_NEURONS"]) * CONFIG["BASE_SYNAPSE_WEIGHT"]
        synapses.diagonal().add_(150.0)  # Рекуррентные контуры самоподдержания
        v_thresholds = torch.ones(CONFIG["N_NEURONS"]) * CONFIG["V_THRESH_BASE"]

    # Инициализация следа памяти (Eligibility Trace) для улучшенного STDP
    trace = torch.zeros((CONFIG["N_NEURONS"], CONFIG["N_NEURONS"]))

    # Таймер для отслеживания 15-секундных интервалов автосохранения
    last_save_time = time.time()

    # Главный защищенный блок симуляции с автосохранением по таймеру и при выходе
    try:
        for t_run in t_run_values:
            steps = int(t_run * 1000)

            for step in range(steps):
                current_time = time.time()

                # ⏱️ АВТОСОХРАНЕНИЕ КАЖДЫЕ 15 СЕКУНД РЕАЛЬНОГО ВРЕМЕНИ
                if current_time - last_save_time >= CONFIG["AUTOSAVE_INTERVAL_SEC"]:
                    os.makedirs(os.path.dirname(CONFIG["CHECKPOINT_PATH"]), exist_ok=True)
                    torch.save({
                        "synapses": synapses,
                        "v_thresholds": v_thresholds
                    }, CONFIG["CHECKPOINT_PATH"])
                    last_save_time = current_time
                    if logger:
                        logger.log("💾 [АВТОБЭКАП]: Опыт успешно сохранен на диск (каждые 15 сек).")

                # 1. Динамическая физика мембран на основе нейрохимии
                v_rest_dynamic = CONFIG["V_REST_BASE"] - (chem.levels["gaba"] * 10.0)
                v_thresh_dynamic = CONFIG["V_THRESH_BASE"] + (chem.levels["serotonin"] * 8.0)
                
                # Учет индивидуального утомления нейронов (Adaptive Thresholds)
                active_thresholds = v_thresh_dynamic + (v_thresholds - CONFIG["V_THRESH_BASE"])
                
                effective_synapses = synapses * chem.levels["acetylcholine"]
                
                noise_amplitude = (7.5 * chem.levels["glutamate"] * chem.levels["histamine"]) 
                noise_amplitude += (chem.levels["stress_crh"] * 15.0)

                # 2. Вычисление токов
                stimulus = torch.randn(CONFIG["N_NEURONS"]) * noise_amplitude
                if chem.levels["endocannabinoids"] > 0.5:
                    stimulus *= 0.3

                voltages += stimulus
                spikes = voltages >= active_thresholds
                num_spikes = torch.sum(spikes).item()

                if num_spikes > 0:
                    voltages[spikes] = CONFIG["V_RESET"]
                    v_thresholds[spikes] += 4.0  # Нейрон временно "устает" от спайка

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

                        # Накопление следа памяти (Eligibility Trace)
                        trace = trace * 0.95 + torch.mm(spikes_matrix.t(), spikes_matrix)

                        # 4. Модификация связей (STDP) и биохимическая реакция
                        if dist <= CONFIG["TARGET_RADIUS"]:
                            chem.inject("dopamine", 25.0) # Агрессивное подкрепление
                            chem.inject("oxytocin", 1.5)
                            chem.inject("stress_crh", -1.0)
                            
                            learning_rate = 1.0 / (0.5 + chem.levels["oxytocin"])
                            synapses += learning_rate * chem.levels["dopamine"] * trace
                            synapses = torch.clamp(synapses, -2000.0, 2000.0) # Защита от перенасыщения
                            
                            voltages += (chem.levels["dopamine"] * 2.0)

                            if logger:
                                logger.log(f"🟢 [ПОДКРЕПЛЕНИЕ]: {action_desc} | Дофамин: {chem.levels['dopamine']:.2f}")
                        else:
                            chem.inject("octopamine", 3.0)
                            chem.inject("stress_crh", 2.0)
                            chem.inject("dopamine", -2.0)

                            synapses -= chem.levels["octopamine"] * trace
                            synapses = torch.clamp(synapses, -2000.0, 2000.0)

                            if logger:
                                logger.log(f"🔴 [ОШИБКА]: {action_desc} | Октопамин: {chem.levels['octopamine']:.2f} | CRH: {chem.levels['stress_crh']:.2f}")

                # 5. Возврат к гомеостазу и релаксация порогов
                voltages = v_rest_dynamic + (voltages - v_rest_dynamic) * CONFIG["BASE_DECAY"]
                v_thresholds = CONFIG["V_THRESH_BASE"] + (v_thresholds - CONFIG["V_THRESH_BASE"]) * 0.97
                chem.update_homeostasis()

    except KeyboardInterrupt:
        print("\n⚠️ Прерывание симуляции пользователем.")
    finally:
        os.makedirs(os.path.dirname(CONFIG["CHECKPOINT_PATH"]), exist_ok=True)
        torch.save({
            "synapses": synapses,
            "v_thresholds": v_thresholds
        }, CONFIG["CHECKPOINT_PATH"])
        print(f"💾 Навыки и опыт мозга успешно сохранены в: {CONFIG['CHECKPOINT_PATH']}")

    return {}
