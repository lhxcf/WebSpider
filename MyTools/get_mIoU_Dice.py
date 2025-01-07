import os
from tqdm import tqdm
import cv2
import numpy as np
from sklearn.metrics import f1_score


# 预测文件目录
prediction_dir = r'E:\郑的江山社稷\论文复现\Models\ImageSegmentation (Unet)\test_result'

# 标签文件目录
label_dir = r'E:\郑的江山社稷\论文复现\Dataset\Lung_COVID\test\masks'

# 计算结果保存位置
test_result_path = r'E:\郑的江山社稷\论文复现\Models\ImageSegmentation (Unet)\test_result_mIoU.txt'

# 前景和背景的标签
FOREGROUND = 1
BACKGROUND = 0


def computer_dice(mask_dir, label_dir_):
    '''
    计算Dice并打印结果
    :param mask_dir: 预测结果，png格式
    :param label_dir_: 标签文件地址
    :return:
    '''
    dice_list = []
    name_list = os.listdir(mask_dir)
    with tqdm(name_list, desc="calculate dice...") as pbar:
        for name in pbar:
            mask = cv2.imread(os.path.join(mask_dir, name), cv2.IMREAD_GRAYSCALE)
            label = cv2.imread(os.path.join(label_dir_, name), cv2.IMREAD_GRAYSCALE)
            if mask.shape != label.shape:
                mask = cv2.resize(mask, (label.shape[1], label.shape[0]))
            mask = (mask / 255).ravel().astype(np.int)
            label = (label / 255).ravel().astype(np.int)
            dice = f1_score(y_true=label, y_pred=mask)
            dice_list.append(dice)

    global info
    info += f'\n Dice : {sum(dice_list) * 1.0 / len(dice_list)}'

    print(f'Dice : {sum(dice_list) * 1.0 / len(dice_list)}')


def calculate_iou(pred_mask, label_mask, class_label):
    """
    计算单个类别（前景或背景）的IoU
    """
    # 获取该类别的预测和标签掩码
    pred_class_mask = (pred_mask == class_label).astype(np.uint8)
    label_class_mask = (label_mask == class_label).astype(np.uint8)

    # 计算交集区域
    intersection = np.sum(pred_class_mask & label_class_mask)
    # 计算并集区域
    union = np.sum(pred_class_mask | label_class_mask)

    # 如果并集为0，则返回0（避免除以零的错误）
    if union == 0:
        return 0.0

    # 计算IoU
    iou = intersection / union
    return iou


def calculate_miou_with_background(prediction_dir_, label_dir_):
    """
    计算给定目录下的所有图像的mIoU，包括前景和背景
    """
    foreground_ious = []
    background_ious = []

    for img_name in tqdm(os.listdir(prediction_dir_), desc='calculate mIoU...'):
        if img_name.endswith('.png'):
            pred_path = os.path.join(prediction_dir_, img_name)
            label_path = os.path.join(label_dir_, img_name)
            assert os.path.exists(pred_path), f"pred_path is not exist"
            # 读取预测和标注掩码
            pred_mask = cv2.imread(pred_path, cv2.IMREAD_GRAYSCALE)
            label_mask = cv2.imread(label_path, cv2.IMREAD_GRAYSCALE)

            # 将掩码转换为二值（如果它们不是已经是的话）
            # 这里假设掩码中的非零值表示前景，零值表示背景
            pred_mask = (pred_mask > 0).astype(np.uint8)
            label_mask = (label_mask > 0).astype(np.uint8)

            # 计算前景和背景的IoU
            foreground_iou = calculate_iou(pred_mask, label_mask, FOREGROUND)
            background_iou = calculate_iou(pred_mask, label_mask, BACKGROUND)

            # 存储IoU值
            foreground_ious.append(foreground_iou)
            background_ious.append(background_iou)

    # 计算平均IoU
    foreground_miou = np.mean(foreground_ious) if foreground_ious else 0.0
    background_miou = np.mean(background_ious) if background_ious else 0.0

    # 计算总的mIoU（这里简单地对前景和背景的IoU取平均，但通常只计算前景的mIoU）
    # 注意：这种计算方式可能不是标准的，因为背景通常不被视为一个需要优化的类别
    # 在实际应用中，可能需要根据具体情况调整mIoU的计算方法
    total_miou = (foreground_miou + background_miou) / 2 if (foreground_ious and background_ious) else 0.0

    return foreground_miou, background_miou, total_miou


if __name__ == "__main__":
    # 计算mIoU，包括前景和背景
    foreground_miou, background_miou, total_miou = calculate_miou_with_background(prediction_dir, label_dir)

    # 打印结果
    info = f'前景类的IoU: {foreground_miou}\n背景类的IoU: {background_miou}\n总的mIoU（包括前景和背景）: {total_miou}'
    print(f'前景类的IoU: {foreground_miou}')
    print(f'背景类的IoU: {background_miou}')
    print(f'总的mIoU（包括前景和背景）: {total_miou}')

    # 计算Dice
    computer_dice(prediction_dir, label_dir)

    # 将结果保存到文件
    with open(test_result_path, 'w', encoding='utf-8') as f:
        f.write(info)