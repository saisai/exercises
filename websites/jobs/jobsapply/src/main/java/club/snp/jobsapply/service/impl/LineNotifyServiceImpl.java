package club.snp.jobsapply.service.impl;

import club.snp.jobsapply.service.LineNotifyService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.util.LinkedHashMap;
@Service
public class LineNotifyServiceImpl implements LineNotifyService {
    @Value("${line.notify.url}")
    private String LINE_NOTIFY_URL;

    @Value("${line.notify.token}")
    private String TOKEN;

    @Override
    public LinkedHashMap<String, Object> sendLineNotifyMessages(String msg) throws Exception {
        MultiValueMap<String, Object> map = new LinkedMultiValueMap<>();
        map.add("message", msg);
        return callLineNotify(map);
    }

    @Override
    public LinkedHashMap<String, Object> sendLineNotifySticker(String msg, int stickerPackageId, int stickerId)
            throws Exception {
        MultiValueMap<String, Object> map = new LinkedMultiValueMap<>();
        map.add("message", msg);
        map.add("stickerPackageId", stickerPackageId);
        map.add("stickerId", stickerId);
        return callLineNotify(map);
    }

    @Override
    public LinkedHashMap<String, Object> sendLineNotifyImagePath(String msg, String imagePath) throws Exception {
        MultiValueMap<String, Object> map = new LinkedMultiValueMap<>();
        map.add("message", msg);
        map.add("imageThumbnail", imagePath);
        map.add("imageFullsize", imagePath);
        return callLineNotify(map);
    }

    @Override
    public LinkedHashMap<String, Object> sendLineNotifyImage(String msg, MultipartFile file) throws Exception {
        MultiValueMap<String, Object> map = new LinkedMultiValueMap<>();
        map.add("message", msg);
        map.add("imageFile", file.getResource());
        return callLineNotify(map);
    }

    @SuppressWarnings("unchecked")
    private LinkedHashMap<String, Object> callLineNotify(MultiValueMap<String, Object> map) throws Exception {
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders headers = new HttpHeaders();
        if (map.get("imageFile") != null) {
            headers.setContentType(MediaType.MULTIPART_FORM_DATA);
        } else {
            headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        }
        headers.add("Authorization", "Bearer " + TOKEN);
        HttpEntity<MultiValueMap<String, Object>> request = new HttpEntity<>(map, headers);
        return restTemplate.postForObject(LINE_NOTIFY_URL, request, LinkedHashMap.class);
    }


}
