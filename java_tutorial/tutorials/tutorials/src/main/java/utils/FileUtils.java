package utils;

import java.io.File;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Paths;

public class FileUtils {

    public File getResourceFile(final String fileName)
    {
        URL url = this.getClass()
                .getClassLoader()
                .getResource(fileName);

        if(url == null) {
            throw new IllegalArgumentException(fileName + " is not found 1");
        }

        File file = new File(url.getFile());

        return file;
    }

    public static String getFileName(String name) throws URISyntaxException {

        //String fullPath = Paths.get(FileUtils.class.getResource(name).toURI()).toString();
        String fileName = String.valueOf(Paths.get(FileUtils.class.getResource(name).toURI()).getFileName());

        //System.out.println("file " + fullPath);
        System.out.println("fileName " + fileName);
        //return fullPath;
        return "test";
    }
}
