import pprint
import json

# основной конфиг
main_config = {
    "project-description": "автоматизированная насосная станция для ОАО СОЮЗ-Энерго",
    "date": "15.04.2021",
    'devices':
        [
            {
                'device-id': 'upp-motor-1',
                'type': 'upp_ve',
                'version': 'v1.01',
                'description': 'Основное УПП на 4кв для запуска качалки',
                'connection': 'upp_motor_1_connection.json',
                'model': 'upp_ve_1_01_model.json',
                'default-web-interface': 'upp_ve_index.html',
            },
            {
                'device-id': 'upp-motor-reserve',
                'type': 'upp_ve',
                'version': 'v1.01',
                'description': 'Резервное УПП на 4кв для запуска качалки',
                'connection': 'upp_motor_reserve_connection.json',
                'model': 'upp_ve_1_01_model.json',
                'default-web-interface': 'upp_ve_index.html',
            },
        ],
    'layouts':
        {
            'web': 'web_layout.json',
            'desktop_v1': 'desktop_v1_layout.json',
            'desktop_v2': 'desktop_v1_layout.json',
            'android': 'android_layout.json',
        },
    'archive': {
        'URI': 'postgres://USERNAME:PASSWORD@babar.elephantsql.com:5432/jszlmeae',
        'archive_schema': 'archive_schema.json',
    }
}

model_config = {
    'registers': {
        'discrete-inputs': [[0, 10], [20, 25]],
        'coils': [[0, 10]],
        'input-registers': [[0, 64], [65, 128]],
        'holding': [[0, 64]],
    },

    'parameters': [
        {
            'parameter-name': 'current',
            'description': 'ток фазы А (А)',
            'model': {
                'register-type': 'holding',
                'type': 'int16',
                'address': 0,
            },
            'view': {
                'type': 'int',
                'min-value': 0,
                'max-value': 1200,
                'change-step': 1,
                'format': '%s А',
                'read-only': True,
            },
        },
        {
            'parameter-name': 'work-mode',
            'description': 'режим работы',
            'model': {
                'register-type': 'holding',
                'type': 'int16',
                'address': 1,
            },
            'view': {
                'type': 'enum',
                'min-value': 0,
                'max-value': 2,
                'change-step': 1,
                'format': '%s',
                'read-only': True,
                'values': [
                    'прямой пуск',
                    'плавный пуск',
                    'форсированный пуск'
                ]
            }
        }
    ]
}

# сохраняем основной конфиг в виде json-файла
with open('main_config.json', 'wt', encoding='utf-8') as f:
    json.dump(main_config, f, ensure_ascii=False, indent=4)

with open('model_config.json', 'wt', encoding='utf-8') as f:
    json.dump(model_config, f, ensure_ascii=False, indent=4)

# with open('main_config.json', 'rt', encoding='utf-8') as f:
#     main_config = json.load(f)
#
# pprint.pprint(main_config)
