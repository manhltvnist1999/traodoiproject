Tổng quan: Nhận dạng người nói sử dụng mfcc để trích xuất âm thanh
và sử dụng Gaussian mixture model (GMM) để phân loại

Các công nghệ sử dụng:
    + python 3.7
    + python_speech_features
    + numpy
    + sklearn
    + scikit-learn

Cách sử dụng:
    + clone prj về từ github
    + cài đặt các công nghệ cần thiết
    + nếu là người lần đầu dùng sản phẩm, bạn cần thu 5 bản ghi âm để
tạo model cho chính bạn. Hãy chạy file train.py để thu 5 bản ghi và được traindata
    + nếu bạn đã traindata của bạn, thì có thể chay file demo.py để
thu âm 1 bản ghi và xem kết quả nhận dạng
