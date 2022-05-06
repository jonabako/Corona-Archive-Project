-- For testing
INSERT INTO `Agent` (`username`, `password`) VALUES ('testname','testpassword');
INSERT INTO `Hospital` (`username`, `password`) VALUES ('testname', 'testpassword');

INSERT INTO `Places` (`place_name`, `address`, `email`, `phone_number`, `QRcode`) VALUES ('test place','test address N200', 'email@email.com', '1111111111111','test-qr-code');

-- Insert sample users for testing
INSERT INTO `Visitor`(`visitor_name`, `address`, `email`, `phone_number`, `device_id`, `infected`)
             VALUES ('Tfname Tlname', 'Test Address 123', 'test@testemail.com', '+123123123123' ,'test-123', 0);
