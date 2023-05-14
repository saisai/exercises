package xyz.blogpost.service;

import org.springframework.web.multipart.MultipartFile;

import java.util.LinkedHashMap;

public interface LineNotifyService {
    LinkedHashMap<String, Object> sendLineNotifyMessages(String msg) throws Exception;
    LinkedHashMap<String, Object> sendLineNotifySticker(String msg, int stickerPackageId, int stickerId) throws Exception;
    LinkedHashMap<String, Object> sendLineNotifyImagePath(String msg, String imagePath) throws Exception;
    LinkedHashMap<String, Object> sendLineNotifyImage(String msg, MultipartFile file) throws Exception;
}
