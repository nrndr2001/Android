package com.example.chirag;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    EditText num;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        num = (EditText) findViewById(R.id.editTextTextnumber);
    }

    public void prime(View view) {
        int n = Integer.parseInt(num.getText().toString());
        int i = 2, flag =0;
        for(i=2; i*i < n; i++){
            if(n%i == 0){
                flag =1;
                break;
            }
        }
        if(flag == 0)
            Toast.makeText(this, "Prime", Toast.LENGTH_SHORT).show();
        else
            Toast.makeText(this, "Not Prime", Toast.LENGTH_SHORT).show();
    }
}