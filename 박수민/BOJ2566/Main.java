import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int[][] nums = new int[9][9];	// 9*9의 숫자를 입력받을 2차원배열
		int max = 0;	// 최댓값 max (초기값 0)
		int[] point = new int[2];	// 최댓값의 위치를 저장할 1차원배열
		for(int i = 0; i < 9; i++) {
			String input = br.readLine();
			st = new StringTokenizer(input);
			for(int j = 0; j < 9; j++) {
				nums[i][j] = Integer.parseInt(st.nextToken()); // i행j열에 입력
				if(nums[i][j] > max) { // if문을 통해 기존의 max보다 nums[i][j]가 더 크면 max를 변경 및 인덱스 저장
					max = nums[i][j];	
					point[0] = i; 
					point[1] = j;
				}
			}
		}
		System.out.println(max);
		System.out.println((point[0]+1) + " " + (point[1]+1)); // 배열은 0부터 시작하니 각각 +1
		
		
	}
}

