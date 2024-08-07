import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[][] nums = new int[100][100];	// 도화지 크기가 100*100
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		for(int i = 0; i < n; i++) {
			String input = br.readLine();
			st = new StringTokenizer(input);
			int a = Integer.parseInt(st.nextToken());	//a,b좌표입력
			int b = Integer.parseInt(st.nextToken()); 
			for(int j = a; j < a+10; j++) {		//a,b부터 a+10,b+10까지 색칠(1로값을바꿔줌)
				for(int m = b; m <b+10; m++) {
					nums[j][m] = 1;
				}
			}
		}
		int result = 0;	// 답넣을 변수
		for(int[] i : nums) {	//for문으로 nums배열(도화지)를 돌며 1인 인덱스를 체크 후 result에 더함 
			for(int j : i) {
				if(j == 1) {
					result++;
				}
			}
		}
		System.out.println(result);
		
	}
}

