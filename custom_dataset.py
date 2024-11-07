import os
from pycocotools.coco import COCO
from data.coco import COCODetection

class CustomDataset(COCODetection):
    def __init__(self, image_path, info_file, transform=None):
        super().__init__(image_path, info_file, transform)

    def __getitem__(self, index):
        # COCO 데이터셋에서 이미지 및 어노테이션 ID 불러오기
        image_id = self.ids[index]
        path = self.coco.loadImgs(image_id)[0]['file_name']
        
        # '_albu'와 '_Gaussian'이 포함된 파일은 건너뛰기
        if '_albu' in path or '_Gaussian' in path:
            return None  # 이 경우, 호출한 코드에서 None 처리를 해줘야 함

        # 이미지 경로 설정 및 이미지 로드
        img_path = os.path.join(self.image_path, path)
        image = super().load_image(image_id)
        
        # 어노테이션 정보 불러오기
        target = self.load_annotations(image_id)
        
        # Transform이 있으면 이미지 및 어노테이션에 적용
        if self.transform is not None:
            image, target = self.transform(image, target)
        
        return image, target
