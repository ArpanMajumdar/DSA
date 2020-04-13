package com.arpan.dsa.exceptions;

public class QueueUnderflowException extends RuntimeException{
    public QueueUnderflowException(String message) {
        super(message);
    }
}

