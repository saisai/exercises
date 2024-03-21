package map.convert;

import org.example.map.convert.StringToMap;
import org.junit.Assert;
import org.junit.jupiter.api.Test;

import java.util.Map;

public class StringToMapUnitTest {

    @Test
    public void givenString_WhenUsingStream_ThenResultingStringIsCorrect() {
        Map<String, String> wordsByKey = StringToMap.convertWithStream("1=one,2=two,3=three,4=four");
        Assert.assertEquals(4, wordsByKey.size());
        Assert.assertEquals("one", wordsByKey.get("1"));
    }
    @Test
    void givenString_WhenUsingGuava_ThenResultingStringIsCorrect() {
        Map<String, String> wordsByKey = StringToMap.convertWithGuava("1=one,2=two,3=three,4=four");
        Assert.assertEquals(4, wordsByKey.size());
        Assert.assertEquals("one", wordsByKey.get("1"));
    }
}

// https://github.com/eugenp/tutorials/blob/master/core-java-modules/core-java-collections-maps-2/src/test/java/com/baeldung/map/convert/StringToMapUnitTest.java