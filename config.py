from data.config import coco_base_config

my_dataset_config = coco_base_config.copy({
    'name': 'TOMATO Dataset',
    'train_images': 'D:/JOLJAK/TOMATO_Train/images/',  # 실제 학습 이미지 경로
    'valid_images': 'D:/JOLJAK/TOMATO_Train/images/',  # 실제 검증 이미지 경로
    'train_info': 'D:/JOLJAK/TOMATO_Train/annotations/instances_train.json',  # 학습 어노테이션 파일
    'valid_info': 'D:/JOLJAK/TOMATO_Train/annotations/instances_val.json',  # 검증 어노테이션 파일
    'num_classes': 3,  # 클래스 개수 (예: 3개 클래스)
    'max_size': 550,  # 이미지 크기 조정
    'lr': 0.001,      # 학습률 (필요시 추가 조정)
    'batch_size': 8,  # 배치 크기 (필요시 추가 조정)
    'use_square_anchors': True,  # 필요시 다른 설정 추가 가능
})
