import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = new String[5];	// 5개의 문자열을 받을 배열
		int maxlen = 0;
		for(int i = 0; i < 5; i++) {
			s[i] = br.readLine();	// 입력
			if(maxlen < s[i].length())	// 제일 긴 문자열의 길이 저장
				maxlen = s[i].length();
		}
		for(int i = 0; i < maxlen; i++) {	// 제일긴 문자열까지 넣기 위해 maxlen이용
			for(int j = 0; j < 5; j++) {	//5개 번갈아가며 출력
				if(s[j].length() > i) {	//j번째문자열의 길이가 i보다 클 경우에만 출력
					System.out.print(s[j].charAt(i));
				}
			}
		}
		
		
	}
}

